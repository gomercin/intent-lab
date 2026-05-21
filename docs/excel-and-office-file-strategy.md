# Excel and Office File Strategy

Excel files are often the source of hidden complexity.

Do not parse complex Excel files directly inside business logic every time.

## Recommended Pipeline

```text
Office file
→ extractor script
→ normalized intermediate data
→ validation
→ business rules
→ action/report
```

## Why Separate Extraction?

Separate extractor scripts help because they:

- isolate messy file handling,
- make debugging easier,
- make output inspectable,
- avoid repeated parsing,
- support large files better,
- reduce coupling with business logic,
- help agents inspect extracted data.

## Office File Internals

Modern Office files like `.xlsx` and `.xlsm` are ZIP-based packages.

For large files or files with macros, it can be useful to inspect the internal XML/files directly instead of loading the entire workbook with heavy libraries.

This can help when:

- only one sheet/table is needed,
- files are large,
- workbook libraries are slow,
- VBA macros must be preserved,
- hidden XML/table structure is more reliable than rendered workbook behavior.

## Macro Files

For `.xlsm` files:

- preserve macros unless explicitly asked to modify them,
- avoid rewriting the workbook if not needed,
- prefer reading/extracting data only,
- keep original files untouched.

## Validation Checklist

Validate:

- required sheet exists,
- required columns exist,
- expected headers are found,
- required cells are not empty,
- dates parse correctly,
- numbers are interpreted correctly,
- IDs are treated as text when needed,
- leading zeros are preserved,
- duplicates are detected,
- unknown statuses are reported,
- formulas are handled correctly,
- hidden/filtered rows are considered intentionally.

## Intermediate Output

Extractor should create something inspectable, such as:

- CSV,
- JSON,
- Parquet,
- normalized Excel,
- validation report.

Store extracted data under:

```text
extracted/
runs/<timestamp>/extracted-data/
```

## Agent Prompt Template

```text
Before implementing business logic, create or review a separate extraction step.

The extractor should:
- read the input Office file safely,
- preserve macros if present,
- extract only relevant data where possible,
- normalize column names,
- preserve important IDs as text,
- produce inspectable intermediate output,
- produce validation errors for missing or inconsistent data.

Do not mix raw Excel parsing, business rules, and UI execution in one large script.
```
