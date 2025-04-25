# -*- coding: utf-8 -*-
import re
import sys
from pathlib import Path
from translations import translations


def arabic_to_python(code):
    for arabic, eng in translations.items():
        # استبدال الكلمات الكاملة فقط
        code = re.sub(rf'\b{arabic}\b', eng, code)
    return code


def transpile_file(input_path, output_path=None):
    input_path = Path(input_path)
    if not input_path.exists():
        print(f" الملف غير موجود: {input_path}")
        return

    code = input_path.read_text(encoding='utf-8')
    translated_code = arabic_to_python(code)

    if output_path is None:
        output_path = Path("build") / input_path.with_suffix(".py").name
    else:
        output_path = Path(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(translated_code, encoding='utf-8')
    print(f" تم التحويل: {input_path} → {output_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(" الاستعمال: python arabicpy.py ملف.pyar")
        sys.exit(1)

    transpile_file(sys.argv[1])

