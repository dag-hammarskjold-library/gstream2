<template>
    <div class="bg-white shadow-md rounded-lg overflow-hidden">
        <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
                <tr>
                    <th v-for="header in headers" :key="header.key"
                        class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer"
                        @click="$emit('sort', header.key)">
                        {{ header.label }}
                        <span v-if="sortKey === header.key" class="ml-1">
                            {{ sortOrder === 'asc' ? '↑' : '↓' }}
                        </span>
                    </th>
                </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="doc in documents" :key="doc.symbol1">
                    <td class="px-6 py-4 whitespace-nowrap">{{ doc.symbol1 }}</td>
                    <td class="px-6 py-4 whitespace-nowrap">{{ doc.symbol2 }}</td>
                    <td class="px-6 py-4">{{ doc.title }}</td>
                    <td class="px-6 py-4">
                        <span v-for="file in doc.files" :key="file.id" class="inline-block mr-2">
                            {{ file.language }}
                        </span>
                    </td>
                    <td class="px-6 py-4">
                        <p v-for="link in doc.links">
                            <a :href="link['url']">{{ link['name'] }}</a>
                        </p>
                        <!--<pre class="text-sm">{{ JSON.stringify(doc.links, null, 2) }}</pre>-->
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script setup lang="ts">
import type { Document, TableHeader } from '~/types/document'

defineProps<{
    documents: Document[]
    headers: TableHeader[]
    sortKey: keyof Document
    sortOrder: 'asc' | 'desc'
}>()

defineEmits<{
    (e: 'sort', key: keyof Document): void
}>()
</script>