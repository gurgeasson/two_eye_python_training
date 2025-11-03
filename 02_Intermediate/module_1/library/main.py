from data.chapters import chapters

for chapter_number, chapter in enumerate(chapters, start=1):
    print(f"{chapter_number}: {chapter}")