from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class KeywordNote:
    keyword: str
    note: str
    tags: List[str] = field(default_factory=list)
    source_url: Optional[str] = None
    created_at: datetime = field(default_factory=datetime.now)

    def formatted_output(self) -> str:
        tags_str = ", ".join(self.tags) if self.tags else "无标签"
        url_str = self.source_url if self.source_url else "无来源"
        return (
            f"关键词: {self.keyword}\n"
            f"笔记:   {self.note}\n"
            f"标签:   {tags_str}\n"
            f"来源:   {url_str}\n"
            f"创建时间: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}\n"
        )

@dataclass
class KeywordNoteCollection:
    notes: List[KeywordNote] = field(default_factory=list)

    def add_note(self, note: KeywordNote) -> None:
        self.notes.append(note)

    def find_by_keyword(self, keyword: str) -> List[KeywordNote]:
        return [note for note in self.notes if keyword.lower() in note.keyword.lower()]

    def find_by_tag(self, tag: str) -> List[KeywordNote]:
        return [note for note in self.notes if any(t.lower() == tag.lower() for t in note.tags)]

    def all_formatted(self) -> str:
        if not self.notes:
            return "暂无笔记。"
        return "\n---\n".join(note.formatted_output() for note in self.notes)

    def export_to_file(self, filepath: str) -> None:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(self.all_formatted())


def generate_sample_data() -> KeywordNoteCollection:
    collection = KeywordNoteCollection()

    collection.add_note(
        KeywordNote(
            keyword="leyu",
            note="核心关键词，用于索引门户的内容组织。",
            tags=["核心", "索引"],
            source_url="https://index-portal-leyu.com"
        )
    )

    collection.add_note(
        KeywordNote(
            keyword="leyu 应用",
            note="基于 leyu 关键词构建的应用场景。",
            tags=["应用", "实践"],
            source_url="https://index-portal-leyu.com"
        )
    )

    collection.add_note(
        KeywordNote(
            keyword="leyu 研究",
            note="对 leyu 关键词的深入分析和研究笔记。",
            tags=["研究", "分析"],
            source_url="https://index-portal-leyu.com"
        )
    )

    return collection


def main():
    print("=== 关键词笔记系统 ===")
    print()
    collection = generate_sample_data()
    print("当前笔记列表：")
    print(collection.all_formatted())

    print("\n搜索关键词 'leyu' 的结果：")
    results = collection.find_by_keyword("leyu")
    for note in results:
        print(note.formatted_output())

    print("\n搜索标签 '核心' 的结果：")
    tag_results = collection.find_by_tag("核心")
    for note in tag_results:
        print(note.formatted_output())

    print("\n将笔记导出到文件 'notes_output.txt'...")
    collection.export_to_file("notes_output.txt")
    print("导出完成。")


if __name__ == "__main__":
    main()