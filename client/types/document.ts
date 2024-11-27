export interface DocumentFile {
    languageId: string
    odsNo: string
}

export interface Document {
    symbol1: string
    symbol2: string
    title: string
    files: DocumentFile[]
    links?: any
}

export interface TableHeader {
    key: keyof Document
    label: string
}