<script lang="js">
import VueDatePicker from "@vuepic/vue-datepicker"
import "@vuepic/vue-datepicker/dist/main.css"

export default {
    data() {
        return {
            apiUrl: "http://0.0.0.0:8000",
            dutyStations: [
                [{ label: "Beirut", click: () => this.dutyStation = "Beirut" }],
                [{ label: "Geneva", click: () => this.dutyStation = "GE" }],
                [{ label: "Nairobi", click: () => this.dutyStation = "Nairobi" }],
                [{ label: "New York", click: () => this.dutyStation = "NY" }],
                [{ label: "Vienna", click: () => this.dutyStation = "Vienna" }]
            ],
            symbolData: [],
            columns: [
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
            ],
            dutyStation: 'NY',
            date: null,
            selectedDate: ref(),
            isLoading: false
        }
    },
    async created() {
        const yesterday = () => {
            let d = new Date()
            d.setDate(d.getDate() - 1)
            return d.toISOString().split('T')[0]
        }
        this.date = yesterday()
        this.selectedDate = this.date.replace(/-/g, "/")
    },
    methods: {
        async onSubmit() {
            console.log("submitting")
            this.isLoading = true
            fetch(`${this.apiUrl}/?duty_station=${this.dutyStation}&date=${this.date}`)
                .then(response => {
                    response.json().then(jsonData => {
                        this.symbolData = jsonData
                    }).then(() => this.isLoading = false)
                }).catch(e => console.log(e))
        },
        setDate(value) {
            //selectedDate.value = value
            this.date = value.toISOString().split('T')[0]
        }
    }
}
</script>

<script setup lang="js">
const state = reactive({
    dutyStation: undefined,
    date: undefined
})
</script>

<template>
    <UContainer>
        <UCard>
            <UForm :state="state" @submit="onSubmit">
                <div class="grid gap-4 grid-cols-3">
                    <UFormGroup label="Duty Station" name="dutyStation">
                        <UDropdown :items="dutyStations" v-model="dutyStation">
                            <UButton color="white" :label="dutyStation"
                                trailing-icon="i-heroicons-chevron-down-20-solid" />
                        </UDropdown>
                    </UFormGroup>
                    <UFormGroup label="Choose a Date" name="date">
                        <VueDatePicker id="manual" v-model="selectedDate" format="yyyy-MM-dd"
                            :enable-time-picker="false" @update:model-value="setDate" auto-apply />
                    </UFormGroup>
                    <UButton type="submit"
                        class="inline-flex items-center justify-center rounded-br-lg border border-transparent mt-5">
                        Submit</UButton>
                </div>
            </UForm>
        </UCard>
            <UTable :loading="isLoading"
                :loadingstate="{ icon: 'i-heroicons-arrow-path-20-solid', label: 'Loading...' }"
                :progress="{ color: 'primary', animation: 'carousel' }" class="min-w-full" :columns="columns"
                :rows="symbolData" :ui="{ td: { base: 'max-w-[0] text-balance' } }" />

        <pre>{{ [dutyStation, date] }}</pre>
    </UContainer>
</template>