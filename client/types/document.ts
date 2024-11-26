export interface DocumentFile {
    language: string
    id: string
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