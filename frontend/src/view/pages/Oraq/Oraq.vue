<template>
  <div class="row mr-1  ml-1">
    <v-card width="100%">
      <b-row>
        <b-col lg="4" class="my-1 mr-3">
          <b-input-group size="sm">
            <b-form-input
              v-model="Tablefilter"
              type="search"
              id="filterInput"
              placeholder="فیلتر"
            ></b-form-input>
            <b-input-group-append>
              <b-button :disabled="!Tablefilter" @click="Tablefilter = ''"
                >پاک کردن</b-button
              >
            </b-input-group-append>
          </b-input-group>
        </b-col>
        <b-col lg="4" xxl="4" class="mt-2">
          <b-form-group>
            <b-form-checkbox-group
              v-model="selectedHeaderOptions"
              :options="HeaderOptions"
              @change="TriggerFilteredHeader"
            ></b-form-checkbox-group>
          </b-form-group>
        </b-col>
      </b-row>

      <b-table
        v-bind:thClass="{
          oraq_table_head: smallFontHeader,
          oraq_table_head_small: smallFontHeader
        }"
        class="oraq-table"
        tbody-tr-class="oraq-table-row"
        striped
        sticky-header="470px"
        :busy.sync="isBusy"
        :no-provider-paging="true"
        :sort-desc.sync="sortDesc"
        :sort-by.sync="sortBy"
        sort-direction="desc"
        sort-icon-left
        dense
        :filter="Tablefilter"
        :filter-debounce="2000"
        bordered
        no-border-collapse
        outlined
        small
        hover
        responsive
        :items="tableData"
        :fields="HD"
        @filtered="onFiltered"
      >
        <template #cell(TradeCount)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(TradeVolume)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(TradeValue)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(yesterday)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(last)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(close)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(first)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(low)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(high)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(MinRange)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(MaxRange)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(CountBuy_Haghighi)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(CountBuy_Hoguhgi)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(VolumeBuy_Haghighi)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(VolumeBuy_Hoghughi)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(CountSell_Haghighi)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(CountSell_Hoghughi)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(VolumeSell_Haghighi)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(VolumeSell_Hoghughi)="data">
          <b class="oraq-table-cell">{{ data.value.toLocaleString() }}</b>
        </template>
        <template #cell(closePercent)="data">
          <b v-if="data.value > 0" class="oraq-table-cell-green"
            >{{ data.value }}%</b
          >
          <b v-if="data.value < 0" class="oraq-table-cell-red"
            >{{ data.value }}%</b
          >
          <b v-if="data.value == 0" class="oraq-table-cell"
            >{{ data.value }}%</b
          >
        </template>
        <template #cell(lastPercent)="data">
          <b v-if="data.value > 0" class="oraq-table-cell-green"
            >{{ data.value }}%</b
          >
          <b v-if="data.value < 0" class="oraq-table-cell-red"
            >{{ data.value }}%</b
          >
          <b v-if="data.value == 0" class="oraq-table-cell"
            >{{ data.value }}%</b
          >
        </template>
      </b-table>
    </v-card>
  </div>
</template>
<script>
export default {
  name: "oraq",
  components: {},
  data() {
    return {
      sortDesc: false,
      sortBy: "ticker",
      selectedHeaderOptions: [],
      HeaderOptions: [
        { text: "قیمت دیروز", value: "yesterday" },
        { text: "اطلاعات حقیقی/حقوقی", value: "HH" }
      ],
      smallFontHeader: false,
      isBusy: true,
      tableData: null,
      Tablefilter: "",
      OraqTableHeader: [
        {
          label: "نماد",
          key: "ticker",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "بازار",
          key: "market",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "تعداد معاملات",
          key: "TradeCount",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "حجم معاملات",
          key: "TradeVolume",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "ارزش معاملات",
          key: "TradeValue",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "قیمت دیروز",
          key: "yesterday",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "آخرین قیمت",
          key: "last",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "درصد تغییر آخرین قیمت",
          key: "lastPercent",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "قیمت پایانی",
          key: "close",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "درصد تغییر قیمت پایانی",
          key: "closePercent",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "کف مجاز قیمت",
          key: "MinRange",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "سقف مجاز قیمت",
          key: "MaxRange",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "بالاترین قیمت",
          key: "high",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "کمترین قیمت",
          key: "low",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "اولین قیمت",
          key: "first",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "تعداد خرید حقیقی",
          key: "CountBuy_Haghighi",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "تعداد خرید حقوقی",
          key: "CountBuy_Hoguhgi",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "حجم خرید حقیقی",
          key: "VolumeBuy_Haghighi",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "حجم خرید حقوقی",
          key: "VolumeBuy_Hoghughi",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "تعداد فروش حقیقی",
          key: "CountSell_Haghighi",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "تعداد فروش حقوقی",
          key: "CountSell_Hoghughi",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "حجم فروش حقیقی",
          key: "VolumeSell_Haghighi",
          thClass: "oraq_table_head",
          sortable: true
        },
        {
          label: "حجم فروش حقوقی",
          key: "VolumeSell_Hoghughi",
          thClass: "oraq_table_head",
          sortable: true
        }
      ]
    };
  },
  computed: {
    HD() {
      return this.TriggerFilteredHeader();
    }
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      this.isBusy = true;

      await this.axios

        .get("/api/Oragh")
        .then(response => {
          this.isBusy = false;

          let data = response.data;
          this.tableData = data;
          console.log(data);
        })
        .catch(error => {
          this.isBusy = false;
          console.log(error);
        });
    },
    TriggerFilteredHeader() {
      let header = JSON.parse(JSON.stringify(this.OraqTableHeader));
      let options = this.selectedHeaderOptions;
      let SwCase = 0;
      if (options.length == 0) {
        this.smallFontHeader = false;
        SwCase = 0;
      } else if (options.length == 1) {
        this.smallFontHeader = true;

        if (options[0] == "yesterday") SwCase = 1;
        else if (options[0] == "HH") {
          this.smallFontHeader = true;
          SwCase = 2;
        }
      } else if (options.length == 2) {
        this.smallFontHeader = true;
        SwCase = 3;
      }
      if (this.smallFontHeader == true)
        for (let item of header) {
          item.thClass = "oraq_table_head_small";
        }
      switch (SwCase) {
        case 0:
          header.splice(5, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;
        case 1:
          for (let i = 0; i < 8; i++) header.pop();
          break;
        case 2:
          header.splice(5, 1);
          break;
        case 3:
          break;
        default:
          header.splice(5, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;
      }
      console.log(header);
      return header;
    }
  }
};
</script>
<style>
.oraq_table_head {
  vertical-align: middle !important;
  font-size: 0.9rem !important;
  font-weight: 600 !important ;
}
.oraq_table_head_small {
  vertical-align: middle !important;
  font-size: 0.7rem !important;
  font-weight: 600 !important ;
}
.oraq-table {
  vertical-align: middle !important;
  text-align: center !important;
  font-size: 0.8rem !important;
  line-height: 1 !important;
}
.oraq-table-row:hover {
  background-color: #999999 !important;
}
.oraq-table-cell {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  font-weight: 400;
}
.oraq-table-cell-green {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  color: green;
  font-weight: 400;
}
.oraq-table-cell-red {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  color: red;
  font-weight: 400;
}
.oraq-table-cell-bold {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  font-weight: 600;
}
.oraq-table-row {
  direction: ltr;
  vertical-align: middle !important;
}
</style>
