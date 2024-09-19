<script setup lang="ts">
import VueDatePicker from "@vuepic/vue-datepicker"
import "@vuepic/vue-datepicker/dist/main.css"

const apiUrl = "http://0.0.0.0:8000"

const route = useRoute()
const router = useRouter()
const query = route.query

// Determine or set the duty station
let dutyStation = query.dutyStation ? query.dutyStation : "NY"

// Determine or set the query date
// And deal with the datepicker selection
const selectedDate = ref()
const setDate = (value) => {
    selectedDate.value = value
    date = value.toISOString().split('T')[0]
    router.push({ path: "/", query: { dutyStation: dutyStation, date: date } })
}
const yesterday = () => {
    let d = new Date()
    d.setDate(d.getDate() - 1)
    return d.toISOString().split('T')[0]
}
let date = query.date ? query.date : yesterday()
selectedDate.value = date.replace(/-/g,"/")

router.push({ path: "/", query: { dutyStation: dutyStation, date: date } })

// Set up duty station selections
const dutyStations = [
    [{
        label: "Beirut",
        click: () => {
            router.push({ path: "/", query: { dutyStation: "Beirut", date: date } })
            dutyStation = "Beirut"
        }
    }], [{
        label: "Geneva",
        click: () => {
            router.push({ path: "/", query: { dutyStation: "GE", date: date } })
            dutyStation = "GE"
        }
    }], [{
        label: "Nairobi",
        click: () => {
            router.push({ path: "/", query: { dutyStation: "Nairobi", date: date } })
            dutyStation = "Nairobi"
        }
    }], [{
        label: "New York",
        click: () => {
            router.push({ path: "/", query: { dutyStation: "NY", date: date } })
            dutyStation = "NY"
        }
    }], [{
        label: "Vienna",
        click: () => {
            router.push({ path: "/", query: { dutyStation: "Vienna", date: date } })
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

//const symbolData = [{"agendaNo":"(k) Fund of the United Nations Environment Programme","jobId":"2412033C","symbol1":"A/79/5/Add.7","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"GEN","title":"Financial report and audited financial statements for the year ended 31 December 2023 and Report of the Board of Auditors","files":["C: 2412033C","E: 2412033E","A: 2412033A","R: 2412033R","F: 2412033F","S: 2412033S"],"links":[]},{"agendaNo":"","jobId":"2413143C","symbol1":"(A/79/1) Colour Publication","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"GEN","title":"Work of the Organization: Report of the Secretary-General (Suppl. No. 1)","files":["C: 2413143C","S: 2413143S","E: 2413143E","F: 2413143F","R: 2413143R","A: 2413143A"],"links":[]},{"agendaNo":"","jobId":"2414713A","symbol1":"A/RES/78/325","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"GEN","title":"United Nations Games: Resolution adopted by the General Assembly on 6 September 2024","files":["A: 2414713A","F: 2414713F","S: 2414713S","C: 2414713C","E: 2414713E","R: 2414713R"],"links":[]},{"agendaNo":"","jobId":"2415644A*","symbol1":"A/78/L.110","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"LTD","title":"Modalities of the 2026 United Nations Water Conference to Accelerate the Implementation of Sustainable Development Goal 6: Ensure availability and sustainable management of water and sanitation for all: draft resolution","files":["A: 2415644A*"],"links":[]},{"agendaNo":"","jobId":"2416308A","symbol1":"A/79/342","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"GEN","title":"Letter dated 9 September 2024 from the Permanent Representative of the Democratic People’s Republic of Korea to the United Nations addressed to the Secretary-General","files":["A: 2416308A","E: 2416308E","C: 2416308C","R: 2416308R","S: 2416308S","F: 2416308F"],"links":[]},{"agendaNo":"","jobId":"2416419R","symbol1":"S/AC.49/2024/6","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"GEN","title":"Note verbale dated 11 September 2024 from the Permanent Mission of Egypt to the United Nations addressed to the Chair of the Committee","files":["R: 2416419R","E: 2416419E","F: 2416419F","S: 2416419S","C: 2416419C"],"links":[]},{"agendaNo":"","jobId":"2416427F","symbol1":"A/RES/78/326","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"GEN","title":"World Rural Development Day: Resolution adopted by the General Assembly on 6 September 2024","files":["F: 2416427F","E: 2416427E","C: 2416427C","A: 2416427A","S: 2416427S","R: 2416427R"],"links":[]},{"agendaNo":"","jobId":"2416430A","symbol1":"A/RES/78/328","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"GEN","title":"Enhancing the participation of Indigenous Peoples’ representatives and institutions in meetings of relevant United Nations bodies on issues affecting them: Resolution adopted by the General Assembly on 6 September 2024","files":["A: 2416430A","F: 2416430F","E: 2416430E","R: 2416430R","S: 2416430S","C: 2416430C"],"links":[]},{"agendaNo":"","jobId":"2416431F","symbol1":"A/RES/78/329","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"GEN","title":"Biennialization of the agenda item entitled “Elimination of unilateral extraterritorial coercive economic measures as a means of political and economic compulsion”: Resolution adopted by the General Assembly on 6 September 2024","files":["F: 2416431F","C: 2416431C","E: 2416431E","R: 2416431R","S: 2416431S","A: 2416431A"],"links":[]},{"agendaNo":"","jobId":"2416551R","symbol1":"A/C.2/79/1","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"GEN","title":"Allocation of agenda items to the Second Committee: Note by the Secretariat","files":["R: 2416551R","E: 2416551E","S: 2416551S","F: 2416551F","C: 2416551C","A: 2416551A"],"links":[]},{"agendaNo":"","jobId":"2416640S","symbol1":"S/2024/670","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"GEN","title":"Letter dated 10 September 2024 from the Permanent Representative of the Sudan to the United Nations addressed to the President of the Security Council","files":["S: 2416640S","C: 2416640C","R: 2416640R","F: 2416640F","A: 2416640A","E: 2416640E"],"links":[]},{"agendaNo":"","jobId":"2416664E","symbol1":"S/2024/10/Rev.1/Add.36","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"GEN","title":"Summary statement by the Secretary-General of matters of which the Security Council is seized and of the stage reached in their consideration: addendum","files":["E: 2416664E","F: 2416664F","A: 2416664A","C: 2416664C","S: 2416664S","R: 2416664R"],"links":[]},{"agendaNo":"","jobId":"2416669E","symbol1":"A/C.3/79/1","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"LTD","title":"Allocation of agenda items to the Third Committee: Note by the Secretariat","files":["E: 2416669E","C: 2416669C","F: 2416669F","A: 2416669A","R: 2416669R","S: 2416669S"],"links":[]},{"agendaNo":"","jobId":"2416671R","symbol1":"A/C.3/79/L.1/Add.1","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"LTD","title":"Status of documentation for the Third Committee","files":["R: 2416671R","S: 2416671S","F: 2416671F","E: 2416671E","A: 2416671A","C: 2416671C"],"links":[]},{"agendaNo":"","jobId":"2416675A*","symbol1":"A/ES-10/L.31/Rev.1","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"LTD","title":"Advisory opinion of the International Court of Justice on the legal consequences arising from Israel’s policies and practices in the Occupied Palestinian Territory, including East Jerusalem, and from the illegality of Israel’s continued presence in the Occupied Palestinian Territory : draft resolution","files":["A: 2416675A*"],"links":[]},{"agendaNo":"","jobId":"2416757E","symbol1":"S/Agenda/9725","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"GEN","title":"Provisional agenda for the 9725th meeting of the Security Council","files":["E: 2416757E","C: 2416757C","F: 2416757F","S: 2416757S","A: 2416757A","R: 2416757R"],"links":[]},{"agendaNo":"Committee on the Elimination of Discrimination against Women, 89th session (7 - 25 October 2024, Geneva)","jobId":"2416959E","symbol1":"CEDAW/C/89/2","symbol2":"","area":"UNDOC","sessionNo":"","distributionType":"GEN","title":"Reports by specialized agencies on the implementation of the Convention in areas falling within the scope of their activities: Report of the United Nations Educational, Scientific and Cultural Organization","files":["E: 2416959E"],"links":[]}]

const tableLoading = ref(true)
let symbolData = ref([])

async function submit() {
    console.log("submitting")
    data: symbolData = await useLazyFetch(`${apiUrl}`, {
        query: {
            duty_station: dutyStation,
            date: date
        },
    })
}


// Set up filtering for the results table
const q = ref('')
const filteredRows = computed(() => {
    if (!q.value) {
        return symbolData
    }

    return symbolData.filter((symbols) => {
        return Object.values(symbols).some((value) => {
            return String(value).toLowerCase().includes(q.value.toLowerCase())
        })
    })
})

</script>

<template>
    <UContainer>
        <UCard>
            <div class="flex">Select Duty Station</div>
            <UDropdown :items="dutyStations" :popper="{ placement: 'bottom-start' }">
                <UButton color="white" :label="dutyStation" trailing-icon="i-heroicons-chevron-down-20-solid" />
            </UDropdown>
            <VueDatePicker id="manual" v-model="selectedDate" format="yyyy-MM-dd" :enable-time-picker="false"
                @update:model-value="setDate" auto-apply />
            <UButton @click="submit">Submit</UButton>
        </UCard>
        <div class="flex px-3 py-3.5 border-b border-gray-200 dark:border-gray-700">
            <UInput v-model="q" placeholder="Filter results..." />
        </div>
        <UTable :loading="tableLoading" :loadingstate="{ icon: 'i-heroicons-arrow-path-20-solid', label: 'Loading...' }"
            :progress="{ color: 'primary', animation: 'carousel' }" class="min-w-full" :columns="columns"
            :rows="filteredRows" :ui="{ td: { base: 'max-w-[0] text-balance' } }">

        </UTable>
    </UContainer>
</template>