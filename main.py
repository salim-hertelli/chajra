import os
import model
import languages
from typing import List

def group_files_by_extension(files: List[model.File]):
    ans = dict()
    ext = ""
    for f in files:
        if "." in f.filename:
            ext = f.filename.split(".")[-1]
        if ans.get(ext) is None:
            ans[ext] = []
        ans[ext].append(f)
    return ans

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")

    files = [model.File(parent_dir = dp, filename = f, full_path = os.path.join(dp, f)) for dp, dn, filenames in os.walk(current_dir) for f in filenames]
    files_grouped = group_files_by_extension(files)

    results = {name: model.LanguageSummary(lines = 0, blank = 0) for name in languages._supported_languages}
    
    for ext, ext_files in files_grouped.items():
        if ext == "":
            # files without file extension can be a binary
            # TODO are there interesing files without extension?
            # TODO example .gitignore / sh scripts ...
            continue
        if not languages.is_supported(ext):
            continue
        language_name = languages.get_language_name(ext)
        lines_sum = 0
        blank_sum = 0
        for f in ext_files:
            with open(f.full_path, "r", encoding="utf8", errors="surrogateescape") as file_buffer:
                lines = []
                blank = 0
                for line in file_buffer.readlines():
                    line = line.strip()
                    if line == "":
                        blank += 1
                    else:
                        lines.append(line)
                lines_sum += len(lines)
                blank_sum += blank
        results[language_name].blank += blank_sum
        results[language_name].lines += lines_sum
    results = {ext: r for ext, r in results.items() if r.lines > 0}
    for ext, r in results.items():
        print(ext, r)