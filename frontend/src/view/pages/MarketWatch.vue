<template>
  <div>
    <div class="row mr-2 mb-1">
      <v-card width="100%">
        <div class="row">
          <div class="col-xxl-1 col-lg-1 mr-1 mt-3 dropdown-rtl">
            <!-- <v-select
            label="بازار"
            v-model="tableMarketSelected"
            :items="tableMarketFilters"
            @input="test"
          >
          </v-select> -->
            <span>بازار</span>
            <b-form-select
              label="بازار"
              v-model="tableMarketSelected"
              :options="tableMarketFilters"
              @input="test"
            ></b-form-select>
          </div>
          <!-- <div class="row"> -->
          <!-- type selctor -->
          <!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
          <div class="col-xxl-3 col-lg-3  dropdown-rtl">
            <div>
              <b-form-group label="نوع" label-for="tags-with-dropdown">
                <b-form-tags
                  id="tags-with-dropdown"
                  v-model="tableMarketTypeSelected"
                  no-outer-focus
                  class="mb-2"
                  @input="test"
                >
                  <template v-slot="{ tags, disabled, addTag, removeTag }">
                    <ul
                      v-if="tags.length > 0"
                      class="list-inline d-inline-block mb-2"
                    >
                      <li
                        v-for="tag in tags"
                        :key="tag"
                        class="list-inline-item"
                      >
                        <b-form-tag
                          @remove="removeTag(tag)"
                          :title="tag"
                          :disabled="disabled"
                          variant="info"
                          >{{ tag }}</b-form-tag
                        >
                      </li>
                    </ul>

                    <b-dropdown
                      size="sm"
                      variant="outline-secondary"
                      block
                      menu-class="w-100"
                    >
                      <template #button-content>
                        <b-icon icon="tag-fill"></b-icon> انتخاب
                      </template>
                      <b-dropdown-form @submit.stop.prevent="() => {}">
                        <b-form-group
                          label="جستجو"
                          label-for="tag-search-input"
                          label-cols-md="auto"
                          class="mb-0"
                          label-size="sm"
                          :description="searchDescType"
                          :disabled="disabled"
                        >
                          <b-form-input
                            v-model="TypeSearch"
                            id="tag-search-input"
                            type="search"
                            size="sm"
                            autocomplete="off"
                          ></b-form-input>
                        </b-form-group>
                      </b-dropdown-form>
                      <b-dropdown-divider></b-dropdown-divider>
                      <b-dropdown-item-button
                        v-for="option in TypeAvailableOptions"
                        :key="option"
                        @click="TypeonOptionClick({ option, addTag })"
                      >
                        {{ option }}
                      </b-dropdown-item-button>
                      <b-dropdown-text v-if="TypeAvailableOptions.length === 0">
                        موردی یافت نشد
                      </b-dropdown-text>
                    </b-dropdown>
                  </template>
                </b-form-tags>
              </b-form-group>
            </div>
          </div>
          <!-- %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% -->
          <!-- industry selector -->
          <div class="col-xxl-3 col-lg-3  dropdown-rtl">
            <div>
              <b-form-group label="صنعت" label-for="tags-with-dropdown">
                <b-form-tags
                  id="tags-with-dropdown"
                  v-model="tableMarketIndustrySelected"
                  no-outer-focus
                  class="mb-2"
                  @input="test"
                >
                  <template v-slot="{ tags, disabled, addTag, removeTag }">
                    <ul
                      v-if="tags.length > 0"
                      class="list-inline d-inline-block mb-2"
                    >
                      <li
                        v-for="tag in tags"
                        :key="tag"
                        class="list-inline-item"
                      >
                        <b-form-tag
                          @remove="removeTag(tag)"
                          :title="tag"
                          :disabled="disabled"
                          variant="info"
                          >{{ tag }}</b-form-tag
                        >
                      </li>
                    </ul>

                    <b-dropdown
                      size="sm"
                      variant="outline-secondary"
                      block
                      menu-class="w-100"
                    >
                      <template #button-content>
                        <b-icon icon="tag-fill"></b-icon> انتخاب
                      </template>
                      <b-dropdown-form @submit.stop.prevent="() => {}">
                        <b-form-group
                          label="Search tags"
                          label-for="tag-search-input"
                          label-cols-md="auto"
                          class="mb-0"
                          label-size="sm"
                          :description="searchDescIndustry"
                          :disabled="disabled"
                        >
                          <b-form-input
                            v-model="IndustrySearch"
                            id="tag-search-input"
                            type="search"
                            size="sm"
                            autocomplete="off"
                          ></b-form-input>
                        </b-form-group>
                      </b-dropdown-form>
                      <b-dropdown-divider></b-dropdown-divider>
                      <b-dropdown-item-button
                        v-for="option in IndustryAvailableOptions"
                        :key="option"
                        @click="IndustryonOptionClick({ option, addTag })"
                      >
                        {{ option }}
                      </b-dropdown-item-button>
                      <b-dropdown-text v-if="TypeAvailableOptions.length === 0">
                        موردی یافت نشد
                      </b-dropdown-text>
                    </b-dropdown>
                  </template>
                </b-form-tags>
              </b-form-group>
            </div>
          </div>
          <!-- END OF SANNNAT  -->
          <!-- <div class="mt-5 col-xxl-4 col-lg-4">
            <b-form-group>
              <b-form-checkbox-group
                v-model="selectedHeaderOptions"
                :options="HeaderOptions"
                @change="TriggerFilteredHeader"
              ></b-form-checkbox-group>
            </b-form-group>
          </div> -->
        </div>
        <!-- </div> -->
      </v-card>
    </div>

    <!-- table -->
    <div class="row mr-1  ml-1">
      <v-card width="100%">
        <div class="row">
          <div class="col-4 mr-3 my-1">
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
          </div>
          <div class="col-xxl-4 col-lg-4 mt-1">
            <b-form-group>
              <b-form-checkbox-group
                v-model="selectedHeaderOptions"
                :options="HeaderOptions"
                @change="TriggerFilteredHeader"
              ></b-form-checkbox-group>
            </b-form-group>
          </div>
        </div>

        <b-table
          thClass="marketwatch-table-head"
          class="marketwatch-table"
          tbody-tr-class="marketwatch-table-row"
          striped
          :busy.sync="isBusy"
          sticky-header="370px"
          dense
          :filter="Tablefilter"
          :filter-debounce="3000"
          :sort-desc.sync="sortDesc"
          :sort-by.sync="sortBy"
          sort-direction="desc"
          sort-icon-left
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
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(TradeVolume)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(TradeValue)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(yesterday)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(last)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(close)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(first)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(low)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(high)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(MinRange)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(MaxRange)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(CountBuy_Haghighi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(CountBuy_Hoguhgi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(VolumeBuy_Haghighi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(VolumeBuy_Hoghughi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(CountSell_Haghighi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(CountSell_Hoghughi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(VolumeSell_Haghighi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(VolumeSell_Hoghughi)="data">
            <b class="marketwatch-table-cell">{{
              data.value.toLocaleString()
            }}</b>
          </template>
          <template #cell(closePercent)="data">
            <b v-if="data.value > 0" class="marketwatch-table-cell-green"
              >{{ data.value }}%</b
            >
            <b v-if="data.value < 0" class="marketwatch-table-cell-red"
              >{{ data.value }}%</b
            >
            <b v-if="data.value == 0" class="marketwatch-table-cell"
              >{{ data.value }}%</b
            >
          </template>
          <template #cell(lastPercent)="data">
            <b v-if="data.value > 0" class="marketwatch-table-cell-green"
              >{{ data.value }}%</b
            >
            <b v-if="data.value < 0" class="marketwatch-table-cell-red"
              >{{ data.value }}%</b
            >
            <b v-if="data.value == 0" class="marketwatch-table-cell"
              >{{ data.value }}%</b
            >
          </template>
        </b-table>
      </v-card>
    </div>
  </div>
</template>
<script>
import { mapState } from "vuex";
export default {
  name: "marketwatch",
  components: {},
  data() {
    return {
      // %%%%%%%%%%%% type data %%%%%%%%%%%%

      // %%%%%%%%%%%% type data %%%%%%%%%%%%
      isBusy: true,
      sortDesc: false,
      sortBy: "ticker",
      tableMarketSelected: "همه",
      tableMarketFilters: ["همه", "بورس", "فرابورس"],
      tableMarketTypeSelected: [],
      tableMarketTypeFilters: [],
      tableMarketIndustrySelected: [],
      tableMarketIndustryFilters: [],
      yesterdayEnableTrigger: false,
      EPSEnableTrigger: false,
      moreInfoTrigger: false,
      WebsocketRequest: false,
      selectedHeaderOptions: [],
      HeaderOptions: [
        { text: "قیمت دیروز", value: "yesterday" },
        { text: "EPS", value: "EPS" },
        { text: "اطلاعات حقیقی/حقوقی", value: "HH" }
      ],
      Tablefilter: "",
      // tableData: [],
      TypeSearch: "",
      IndustrySearch: "",
      value: [],
      MarketTableHeader: [
        {
          label: "نماد",
          key: "ticker",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "بازار",
          key: "marketName",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "تعداد معاملات",
          key: "TradeCount",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "حجم معاملات",
          key: "TradeVolume",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "ارزش معاملات",
          key: "TradeValue",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "قیمت دیروز",
          key: "yesterday",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "آخرین قیمت",
          key: "last",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "درصد تغییر آخرین قیمت",
          key: "lastPercent",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "قیمت پایانی",
          key: "close",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "درصد تغییر قیمت پایانی",
          key: "closePercent",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        // { label: "نام", key: "name" },
        // { label: "صنعت", key: "industry" },
        // { label: "آخرین بروز رسانی", key: "updatedAt" },
        {
          label: "کف مجاز قیمت",
          key: "MinRange",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "سقف مجاز قیمت",
          key: "MaxRange",
          thClass: "marketwatch-table-head"
        },
        { label: "EPS", key: "EPS", thClass: "marketwatch-table-head" },
        {
          label: "بالاترین قیمت",
          key: "high",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "کمترین قیمت",
          key: "low",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "اولین قیمت",
          key: "first",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "تعداد خرید حقیقی",
          key: "CountBuy_Haghighi",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "تعداد خرید حقوقی",
          key: "CountBuy_Hoguhgi",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "حجم خرید حقیقی",
          key: "VolumeBuy_Haghighi",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "حجم خرید حقوقی",
          key: "VolumeBuy_Hoghughi",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "تعداد فروش حقیقی",
          key: "CountSell_Haghighi",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "تعداد فروش حقوقی",
          key: "CountSell_Hoghughi",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "حجم فروش حقیقی",
          key: "VolumeSell_Haghighi",
          thClass: "marketwatch-table-head",
          sortable: true
        },
        {
          label: "حجم فروش حقوقی",
          key: "VolumeSell_Hoghughi",
          thClass: "marketwatch-table-head",
          sortable: true
        }
      ]
    };
  },
  // watch: {
  //   selectedHeaderOptions() {
  //     // console.log(this.selectedHeaderOptions);
  //     // this.TriggerFilteredHeader();
  //   }
  // },
  computed: {
    // %%%%%%%%%%%% type data %%%%%%%%%%%%
    Typecriteria() {
      // Compute the search criteria
      return this.TypeSearch.trim().toLowerCase();
    },
    Industrycriteria() {
      // Compute the search criteria
      return this.TypeSearch.trim().toLowerCase();
    },
    TypeAvailableOptions() {
      let criteria = this.TypeSearch;
      // Filter out already selected options
      let options = this.tableMarketTypeFilters.filter(
        opt => this.tableMarketTypeSelected.indexOf(opt) === -1
      );
      if (criteria) {
        // Show only options that match criteria
        return options.filter(opt => opt.indexOf(criteria) > -1);
      }
      // Show all options available
      return options;
    },
    searchDescType() {
      if (this.Typecriteria && this.TypeAvailableOptions.length === 0) {
        return "There are no tags matching your search criteria";
      }
      return "";
    },
    IndustryAvailableOptions() {
      let criteria = this.IndustrySearch;
      // Filter out already selected options
      let options = this.tableMarketIndustryFilters.filter(
        opt => this.tableMarketIndustrySelected.indexOf(opt) === -1
      );
      if (criteria) {
        // Show only options that match criteria
        return options.filter(opt => opt.indexOf(criteria) > -1);
      }
      // Show all options available
      return options;
    },
    searchDescIndustry() {
      if (this.Industrycriteria && this.IndustryAvailableOptions.length === 0) {
        return "There are no tags matching your search criteria";
      }
      return "";
    },
    // %%%%%%%%%%%% type data %%%%%%%%%%%%

    HD() {
      return this.TriggerFilteredHeader();
    },

    ...mapState({
      tableData: state => state.marketwatch.marketWatchItems
    })

    // TableFiltered() {
    //   if (
    //     this.filters.tableMarketTypeSelected.length == 0 &&
    //     this.filters.tableMarketIndustrySelected.length == 0
    //   ) {
    //     return this.tableData;
    //   } else if (this.filters.tableMarketIndustrySelected.length == 0) {
    //     let Tdata = this.tableData;
    //     let temp = [];
    //     for (let obj of Tdata) {
    //       if (this.filters.tableMarketTypeSelected.includes(obj["Type"])) {
    //         temp.push(obj);
    //       }
    //     }
    //     return temp;
    //   } else if (this.filters.tableMarketTypeSelected.length == 0) {
    //     let Tdata = this.tableData;
    //     let temp = [];
    //     for (let obj of Tdata) {
    //       if (
    //         this.filters.tableMarketIndustrySelected.includes(obj["Industry"])
    //       ) {
    //         temp.push(obj);
    //       }
    //     }
    //     return temp;
    //   } else {
    //     let Tdata = this.tableData;
    //     let temp = [];
    //     for (let obj of Tdata) {
    //       if (
    //         this.filters.tableMarketTypeSelected.includes(obj["Type"]) &&
    //         this.filters.tableMarketIndustrySelected.includes(obj["Industry"])
    //       ) {
    //         temp.push(obj);
    //       }
    //     }
    //     return temp;
    //   }
    // }
  },
  mounted() {
    this.loadData();
    this.TriggerFilteredHeader();
    console.log(this.TableFilteredY());
  },
  methods: {
    setFilterSelected() {
      // this.selectedFilters = [
      //   this.filters.tableMarketSelected,
      //   this.filters.tableMarketTypeSelected,
      //   this.filters.tableMarketIndustrySelected
      // ];
      if (this.WebsocketRequest == true) {
        // this.WebsocketRequest = false
        // this.Stop();
        this.MarketWatchFilterPost();
        // this.liveChecker();
      } else {
        this.MarketWatchFilterPost();
        // this.liveChecker();
      }
    },
    test() {
      console.log(this.tableMarketSelected);
      this.MarketWatchFilterPost();
    },
    TriggerFilteredHeader() {
      let header = JSON.parse(JSON.stringify(this.MarketTableHeader));
      let options = this.selectedHeaderOptions;

      let SwCase = 0;
      if (options.length == 0) SwCase = 0;
      else if (options.length == 1) {
        console.log(options);
        if (options[0] == "yesterday") SwCase = 1;
        else if (options[0] == "EPS") SwCase = 2;
        else if (options[0] == "HH") SwCase = 3;
      } else if (options.length == 2) {
        if (!options.includes("HH")) SwCase = 4;
        else if (!options.includes("yesterday")) SwCase = 5;
        else if (!options.includes("EPS")) SwCase = 6;
      } else if (options.length == 3) SwCase = 7;

      switch (SwCase) {
        case 0:
          header.splice(5, 1);
          header.splice(11, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;
        case 1:
          header.splice(12, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;

        case 2:
          header.splice(5, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;
        case 3:
          header.splice(5, 1);
          header.splice(11, 1);
          break;

        case 4:
          for (let i = 0; i < 8; i++) header.pop();
          break;

        case 5:
          header.splice(5, 1);
          break;

        case 6:
          header.splice(12, 1);
          break;

        case 7:
          break;
        default:
          header.splice(5, 1);
          header.splice(11, 1);
          for (let i = 0; i < 8; i++) header.pop();
          break;
      }
      return header;
    },
    onFiltered(filteredItems) {
      // Trigger pagination to update the number of buttons/pages due to filtering
      this.totalRows = filteredItems.length;
      this.currentPage = 1;
    },
    TableFilteredY() {
      if (
        this.tableMarketTypeSelected.length == 0 &&
        this.tableMarketIndustrySelected.length == 0
      ) {
        return this.tableData;
      } else if (this.tableMarketIndustrySelected.length == 0) {
        let Tdata = this.tableData;
        let temp = [];
        for (let obj of Tdata) {
          if (this.tableMarketTypeSelected.includes(obj["Type"])) {
            temp.push(obj);
          }
        }
        return temp;
      } else if (this.tableMarketTypeSelected.length == 0) {
        let Tdata = this.tableData;
        let temp = [];
        for (let obj of Tdata) {
          if (this.tableMarketIndustrySelected.includes(obj["Industry"])) {
            temp.push(obj);
          }
        }
        return temp;
      } else {
        let Tdata = this.tableData;
        let temp = [];
        for (let obj of Tdata) {
          if (
            this.tableMarketTypeSelected.includes(obj["Type"]) &&
            this.tableMarketIndustrySelected.includes(obj["Industry"])
          ) {
            temp.push(obj);
          }
        }
        return temp;
      }
    },
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.MarketWatchTableReq().then(response => {
        this.MarketWatchFilterListReq();
      });
    },
    async MarketWatchTableReq() {
      this.isBusy = true;

      await this.axios
        .get("/api/marketwatch")
        .then(response => {
          this.isBusy = false;

          // let data = response.data;
          // this.tableData = data;
          this.$store.dispatch("setMarketWatchItems", response.data);
          console.log(this.tableData);
        })
        .catch(error => {
          this.isBusy = false;

          console.log(error);
        });
    },
    async MarketWatchFilterListReq() {
      await this.axios.get("/api/marketwatchfilterlists").then(response => {
        this.tableMarketTypeFilters = response.data[0];
        this.tableMarketIndustryFilters = response.data[1];
        // console.log(response.data);
        // let data = response.data[0];
        // let test = this.tableData[0].includes(data[0]);
        // for (let obj of this.tableData) {
        //   if (obj["Type"] == data[0]) console.log(obj);
        // }
      });
    },
    MarketWatchFilterPost() {
      this.axios({
        method: "post",
        url: "/api/marketwatch",
        data: {
          marketName: this.tableMarketSelected,
          marketType: this.tableMarketTypeSelected,
          marketIndustry: this.tableMarketIndustrySelected
        },
        xsrfHeaderName: "X-CSRFToken"
      })
        .then(response => {
          // console.log(response.data);
          this.$store.dispatch("setMarketWatchItems", response.data);
        })
        .catch(error => {
          console.log(error);
        });
    },

    TypeonOptionClick({ option, addTag }) {
      addTag(option);
      this.TypeSearch = "";
      this.MarketWatchFilterPost();
      console.log(option);
    },
    IndustryonOptionClick({ option, addTag }) {
      addTag(option);
      this.IndustrySearch = "";
      this.MarketWatchFilterPost();
      console.log(option);
    }
  }
};
</script>
<style>
.form-input-class {
  direction: rtl;
}
.form-tag-class {
  direction: rtl !important;
}
.dropdown-rtl {
  text-align: right !important;
  direction: rtl;
}
.marketwatch-table-head {
  background-color: #f2f2f2;
  vertical-align: middle !important;
  font-size: 0.9rem !important;
  font-weight: 600 !important ;
}
.marketwatch-table {
  vertical-align: middle !important;
  text-align: center !important;
  font-size: 0.8rem !important;
  line-height: 1 !important;
}
.marketwatch-table-row:hover {
  background-color: #999999 !important;
}
.marketwatch-table-cell {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  font-weight: 400;
}
.marketwatch-table-cell-green {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  color: green;
  font-weight: 400;
}
.marketwatch-table-cell-red {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  color: red;
  font-weight: 400;
}
.marketwatch-table-cell-bold {
  text-align: center;
  font-size: 0.8rem;
  line-height: 1;
  font-weight: 600;
}
.marketwatch-table-row {
  direction: ltr;
  vertical-align: middle !important;
}

/* .selector .v-text-field--box .v-input__slot,
.v-text-field--outlined .v-input__slot {
  min-height: 25px !important;
  max-height: 50px;
  display: flex !important;
  align-items: center !important;
  font-size: 0.8rem !important;
}
.selector .v-chip.v-size--small {
  border-radius: 19px !important;
  font-size: 0.8rem !important;
  height: 19px !important;
  background-color: "#3dbff0";
} */
</style>
