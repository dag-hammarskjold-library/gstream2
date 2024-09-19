<script setup lang="ts">
import VueDatePicker from "@vuepic/vue-datepicker"
import "@vuepic/vue-datepicker/dist/main.css"

const apiUrl = "http://localhost:8000"

const route = useRoute()
const router = useRouter()
const query = route.query

// Determine or set the duty station
let dutyStation = query.dutyStation ? query.dutyStation : "NY"

// Determine or set the query date

const date = ref()
const setDate = (value) => {
    date.value = value
    router.push({ path: "/", query: { dutyStation: dutyStation, date: value.toISOString().split('T')[0] } })
}

// Update the URL in the window location
router.push({ path: "/", query: { dutyStation: dutyStation, date: date.value } })

// Set up duty station selections
const dutyStations = [
    [{
        label: "Beirut",
        click: () => {
            router.push({ path: "/", query: { dutyStation: "Beirut", date: date.value } })
            dutyStation = "Beirut"
        }
    }], [{
        label: "Geneva",
        click: () => {
            router.push({ path: "/", query: { dutyStation: "GE", date: date.value } })
            dutyStation = "GE"
        }
    }], [{
        label: "Nairobi",
        click: () => {
            router.push({ path: "/", query: { dutyStation: "Nairobi", date: date.value } })
            dutyStation = "Nairobi"
        }
    }], [{
        label: "New York",
        click: () => {
            router.push({ path: "/", query: { dutyStation: "NY", date: date.value } })
            dutyStation = "NY"
        }
    }], [{
        label: "Vienna",
        click: () => {
            router.push({ path: "/", query: { dutyStation: "Vienna", date: date.value } })
            dutyStation = "Vienna"
        }
    }]
]

// Set up the table columns
const columns = [
    {
        key: 'symbol1', label: 'Symbol1', sortable: true
    }, {
        key: 'symbol2', label: 'Symbol2', sortable: true
    }, {
        key: 'title', label: 'Title', sortable: true
    }, {
        key: 'links', label: 'Links', sortable: true
    }, {
        key: 'files', label: 'Files'
    }
]

// data we're retrieving
//const { status, data } = await useLazyAsyncData('symbolData', () => $fetch(`${apiUrl}/?duty_station=${dutyStation}&date=${date}`))
const symbolData = []

// Set up filtering for the results table
const q = ref('')
const filteredRows = computed(() => {
    if (!q.value) {
        return symbolData
    }

    return symbolData.filter((symbolData) => {
        return Object.values(symbol1).some((value) => {
            return String(value).toLowerCase().includes(q.value.toLowerCase())
        })
    })
})

const { data } = await useFetch(`${apiUrl}`,
    {
        query: {
            duty_station: dutyStation,
            date: date
        }
    }
)

</script>

<template>
    <UContainer>
        <UCard>
            <div class="flex">Select Duty Station</div>
            <UDropdown :items="dutyStations" :popper="{ placement: 'bottom-start' }">
                <UButton color="white" :label="dutyStation" trailing-icon="i-heroicons-chevron-down-20-solid" />
            </UDropdown>
            <VueDatePicker id="manual" v-model="date" format="yyyy-MM-dd" :enable-time-picker="false"
                @update:model-value="setDate" auto-apply />
        </UCard>
        <div class="flex px-3 py-3.5 border-b border-gray-200 dark:border-gray-700">
            <UInput v-model="q" placeholder="Filter results..." />
        </div>
        <UTable loading :loadingstate="{ icon: 'i-heroicons-arrow-path-20-solid', label: 'Loading...' }"
            :progress="{ color: 'primary', animation: 'carousel' }" class="min-w-full" :columns="columns"
            :rows="filteredRows" :ui="{ td: { base: 'max-w-[0] text-balance' } }" />
        <pre>{{ data }}</pre>
    </UContainer>
</template>