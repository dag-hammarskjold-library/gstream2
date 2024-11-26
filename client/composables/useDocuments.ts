import { ref, type Ref } from 'vue'

interface Document {
    symbol1: string
    symbol2: string
    title: string
    files: Array<{ language: string, id: string }>
    links?: any
}

export function useDocuments() {
    const documents: Ref<Document[]> = ref([])
    const loading = ref(false)
    const error = ref(null)

    const fetchDocuments = async (date: string, dutyStation: string) => {
        loading.value = true
        error.value = null

        try {
            const config = useRuntimeConfig()
            const response = await fetch(`${config.public.apiBase}/?date=${date}&dutyStation=${dutyStation}`)
            const data = await response.json()

            // Fetch additional data for each document
            const documentsWithLinks = await Promise.all(
                data.map(async (doc: Document) => {
                    try {
                        const symbolResponse = await fetch(`${config.public.apiBase}/symbol?symbol=${doc.symbol1}`)
                        const links = await symbolResponse.json()
                        return { ...doc, links }
                    } catch (err) {
                        return { ...doc, links: null }
                    }
                })
            )

            documents.value = documentsWithLinks
        } catch (err: any) {
            error.value = err.message
        } finally {
            loading.value = false
        }
    }

    return {
        documents,
        loading,
        error,
        fetchDocuments
    }
}