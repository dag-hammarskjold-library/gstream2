<template>
    <div class="flex gap-4">
        <div class="w-64">
            <label class="block text-sm font-medium text-gray-700">Date</label>
            <input type="date" :value="modelValue.date"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
                @input="updateFilters('date', ($event.target as HTMLInputElement).value)" />
        </div>

        <div class="w-64">
            <label class="block text-sm font-medium text-gray-700">Duty Station</label>
            <select :value="modelValue.dutyStation"
                class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-indigo-500 focus:ring-indigo-500"
                @change="updateFilters('dutyStation', ($event.target as HTMLSelectElement).value)">
                <option v-for="station in dutyStations" :key="station" :value="station">
                    {{ station }}
                </option>
            </select>
        </div>
    </div>
</template>

<script setup lang="ts">
interface Filters {
    date: string
    dutyStation: string
}

const props = defineProps<{
    modelValue: Filters
    dutyStations: string[]
}>()

const emit = defineEmits<{
    (e: 'update:modelValue', value: Filters): void
}>()

function updateFilters(key: keyof Filters, value: string) {
    emit('update:modelValue', {
        ...props.modelValue,
        [key]: value
    })
}
</script>