import pandas as pd

# ---- Load ----
df = pd.read_csv("HBS1L_MYB_SNP.csv")

# ---- Identify metadata vs frequency columns ----
variant_cols = [
    "chr", "pos", "snp_id", "variant_type",
    "function_class", "validation_status",
    "clinical_significance", "gene"
]
variant_cols = [c for c in variant_cols if c in df.columns]  # keep existing ones
freq_cols = [c for c in df.columns if c not in variant_cols]

# ---- 1️⃣ Clean the variant metadata ----
variants = (
    df[variant_cols]
    .drop_duplicates(subset="snp_id")  # remove duplicate SNPs
    .copy()
)

# -- Fill missing clinical significance with "unknown" --
if "clinical_significance" in variants.columns:
    variants["clinical_significance"] = variants["clinical_significance"].fillna("unknown")

# -- Split semicolon-separated values into lists --
for col in ["function_class", "validation_status"]:
    if col in variants.columns:
        variants[col] = variants[col].astype(str).apply(
            lambda x: [v.strip() for v in x.split(";") if v.strip()] if ";" in x else [x.strip()]
        )

# ---- 2️⃣ Create the long, tidy frequency table (packed strings -> allele, freq, count, source) ----
# We will use the original `df` (not the `variants` table) so we can capture per-row frequencies.

# From 'frequency' onward (includes any Unnamed columns)
if "frequency" not in df.columns:
    raise ValueError("Expected a 'frequency' column. Make sure the file has packed frequency columns.")

start_idx = df.columns.get_loc("frequency")
freq_block_cols = list(df.columns[start_idx:])

# Choose robust identifiers to carry through (only those that exist in df)
id_cols = [c for c in ["snp_id", "chr", "pos", "variation", "variant_type"] if c in df.columns]

# Melt: each packed cell becomes a row
freq_long = (
    df[id_cols + freq_block_cols]
    .melt(id_vars=id_cols, value_vars=freq_block_cols,
          var_name="freq_col", value_name="packed")
)

# Drop blanks
freq_long = freq_long.dropna(subset=["packed"])
freq_long = freq_long[freq_long["packed"].astype(str).str.strip() != ""]

# Split "allele:freq:count:source"
parts = freq_long["packed"].astype(str).str.split(":", n=3, expand=True)
while parts.shape[1] < 4:
    parts[parts.shape[1]] = None
parts = parts.iloc[:, :4]
parts.columns = ["allele", "allele_frequency", "allele_count", "source"]

# Build tidy table
frequencies = pd.concat([freq_long[id_cols].reset_index(drop=True),
                         parts.reset_index(drop=True)], axis=1)

# Coerce numerics
frequencies["allele_frequency"] = pd.to_numeric(frequencies["allele_frequency"], errors="coerce")
frequencies["allele_count"]     = pd.to_numeric(frequencies["allele_count"], errors="coerce")

# Remove exact duplicates (same SNP/source/allele)
dedup_keys = [c for c in ["snp_id", "chr", "pos", "variation", "variant_type", "source", "allele"]
              if c in frequencies.columns]
frequencies = frequencies.drop_duplicates(subset=dedup_keys, keep="first")

# Sort for readability
sort_cols = [c for c in ["snp_id", "chr", "pos", "variant_type", "source", "allele"] if c in frequencies.columns]
frequencies = frequencies.sort_values(sort_cols, kind="stable").reset_index(drop=True)

# ---- 3️⃣ Output checks ----
print("✅ Cleaned variant table:", variants.shape)
print("✅ Long frequency table (tidy):", frequencies.shape)

# Optional: save results (keeps your original variants output)
variants.to_csv("HBSL1L_MYB_clean.csv", index=False)
frequencies.to_csv("HBS1L_MYB_freq.csv", index=False)