<template>
  <div class="card card-custom card-stretch gutter-b">
    <div class="card-header border-0">
      <h3 class="card-title font-weight-bolder FinancialStrength">
        گزارش ماهیانه
        <b-spinner
          class="titleHeaders"
          type="grow"
          small
          v-if="loading"
        ></b-spinner>
      </h3>
    </div>
    <!--end::Header-->
    <!--begin::Body-->
    <div
      class="card-body d-flex flex-column"
      v-if="type == 'bank' && loading == false"
    >
      <v-tabs
        background-color="#3F51B5"
        color="#FFF"
        dark
        prev-icon="mdi-arrow-right-bold-box-outline"
        next-icon="mdi-arrow-left-bold-box-outline"
        show-arrows
      >
        <v-tab
          v-for="item in this.todatesyears"
          :key="item.key"
          @click="GetFilteredYearly(item.value)"
        >
          {{ item.value }}
        </v-tab>
        <v-tab-item v-for="item in this.todatesyears" :key="item.key">
          <v-tabs
            vertical
            background-color="#1A237E"
            color="#FFF"
            dark
            next-icon="mdi-arrow-right-bold-box-outline"
            prev-icon="mdi-arrow-left-bold-box-outline"
            show-arrows
          >
            <v-tab
              v-for="item in todates"
              :key="item.key"
              @click="GetFiltered(item.value)"
            >
              {{ item.value }}
            </v-tab>
            <v-tab-item v-for="itemR in todates" :key="itemR.key">
              <div class="card-body d-flex flex-column">
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    گزارش تسهیلات
                  </h4>
                </div>
                <v-data-table
                  :headers="headersfacility"
                  :items="filteredItems"
                  class="elevation-1 FinancialStrength"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                >
                </v-data-table>
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    گزارش سپرده ها
                  </h4>
                </div>
                <v-data-table
                  :headers="headersdeposit"
                  :items="filteredItems2"
                  class="elevation-1 FinancialStrength"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                >
                </v-data-table>
              </div>
            </v-tab-item>
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>
    <div
      class="card-body d-flex flex-column"
      v-if="type == 'insurance' && loading == false"
    >
      <v-tabs
        background-color="#3F51B5"
        color="#FFF"
        dark
        prev-icon="mdi-arrow-right-bold-box-outline"
        next-icon="mdi-arrow-left-bold-box-outline"
        show-arrows
      >
        <v-tab
          v-for="item in this.todatesyears"
          :key="item.key"
          @click="GetFilteredYearly(item.value)"
        >
          {{ item.value }}
        </v-tab>
        <v-tab-item v-for="item in this.todatesyears" :key="item.key">
          <v-tabs
            vertical
            background-color="#1A237E"
            color="#FFF"
            dark
            next-icon="mdi-arrow-right-bold-box-outline"
            prev-icon="mdi-arrow-left-bold-box-outline"
            show-arrows
          >
            <v-tab
              v-for="item in todates"
              :key="item.key"
              @click="GetFiltered(item.value)"
            >
              {{ item.value }}
            </v-tab>
            <v-tab-item v-for="itemR in todates" :key="itemR.key">
              <div class="card-body d-flex flex-column">
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    گزارش فعالیت بیمه
                  </h4>
                </div>
                <v-data-table
                  :headers="heaadersInsurance"
                  :items="filteredItems"
                  class="elevation-1 FinancialStrength"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                >
                </v-data-table>
              </div>
            </v-tab-item>
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>
    <div
      class="card-body d-flex flex-column"
      v-if="type == 'production' && loading == false"
    >
      <span class="rtl_centerd">production</span>
    </div>

    <div
      class="card-body d-flex flex-column"
      v-if="type == 'leasing' && loading == false"
    >
      <span class="rtl_centerd">leasing</span>
    </div>
    <div
      class="card-body d-flex flex-column"
      v-if="type == 'service' && loading == false"
    >
      <span class="rtl_centerd">service</span>
    </div>
    <div
      class="card-body d-flex flex-column"
      v-if="type == 'construction' && loading == false"
    >
      <v-tabs
        background-color="#3F51B5"
        color="#FFF"
        dark
        prev-icon="mdi-arrow-right-bold-box-outline"
        next-icon="mdi-arrow-left-bold-box-outline"
        show-arrows
      >
        <v-tab
          v-for="item in this.todatesyears"
          :key="item.key"
          @click="GetFilteredYearly(item.value)"
        >
          {{ item.value }}
        </v-tab>
        <v-tab-item v-for="item in this.todatesyears" :key="item.key">
          <v-tabs
            vertical
            background-color="#1A237E"
            color="#FFF"
            dark
            next-icon="mdi-arrow-right-bold-box-outline"
            prev-icon="mdi-arrow-left-bold-box-outline"
            show-arrows
          >
            <v-tab
              v-for="item in todates"
              :key="item.key"
              @click="GetFiltered(item.value)"
            >
              {{ item.value }}
            </v-tab>
            <v-tab-item v-for="itemR in todates" :key="itemR.key">
              <div class="card-body d-flex flex-column">
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    گزارش پروژه های فروخته
                  </h4>
                </div>
                <v-data-table
                  :headers="headersconstructionSold"
                  :items="filteredItems"
                  class="elevation-1 FinancialStrength"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                >
                </v-data-table>
                <div class="card-header border-0">
                  <h4 class="card-title font-weight-bolder FinancialStrength">
                    گزارش پروژه های جاری
                  </h4>
                </div>
                <v-data-table
                  :headers="headersconstructionOngoing"
                  :items="filteredItems2"
                  class="elevation-1 FinancialStrength"
                  :header-props="{ sortIcon: null }"
                  :disable-sort="true"
                  hide-default-footer
                  disable-pagination
                >
                </v-data-table>
              </div>
            </v-tab-item>
          </v-tabs>
        </v-tab-item>
      </v-tabs>
    </div>
    <div
      class="card-body d-flex flex-column"
      v-if="type == '' && loading == false"
    >
      <span class="rtl_centerd">دیتا برای نمایش وجود ندارد</span>
    </div>
  </div>
  <!--end::Mixed Widget 14-->
</template>

<script>
import { mapGetters } from "vuex";
export default {
  name: "MonthlyWidget",
  props: ["notices", "deposits", "typeOf"],
  data() {
    return {
      search: "",
      loading: true,
      type: "",
      todates: [],
      todatesyears: [],
      selectedMonth: "",
      selectedYear: "",
      headersfacility: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        {
          text: "شرکت گزارش دهنده",
          value: "reported_firm"
        },
        {
          text: "عنوان",
          value: "title"
        },
        {
          text: "مانده اول دوره تسهیلات",
          value: "StartPeriod_RemainingFacility"
        },
        {
          text: "اصلاحات",
          value: "StartPeriod_RemainingFacility_modifications"
        },
        {
          text: "مانده اول دوره تسهیلات- اصلاح شده",
          value: "StartPeriod_RemainingFacility_modified"
        },
        {
          text: "تسهیلات اعطایی طی دوره",
          value: "thisPeriod_IssuedFacilitiy"
        },
        {
          text: "تسهیلات وصولی طی دوره",
          value: "thisPeriod_SetteledFacility"
        },
        {
          text: "مانده تسهیلات اعطایی پایان دوره",
          value: "EnePeriod_RemainingFacility"
        },
        {
          text: "درآمد تسهیلات از ابتدای سال مالی تا ابتدای دوره",
          value: "PreviousPeriods_RevenueFromFacility"
        },
        {
          text: "اصلاحات",
          value: "PreviousPeriods_RevenueFromFacility_modification"
        },
        {
          text: "درآمد تسهیلات از ابتدای سال مالی تا ابتدای دوره -اصلاح شده",
          value: "PreviousPeriods_RevenueFromFacility_modified"
        },
        {
          text: " درآمد تسهیلات اعطایی در طی دوره گزارش",
          value: "thisPeriod_RevenueFromFacility"
        },
        {
          text: "جمع درآمد تسهیلات از ابتدای سال مالی تا پایان دوره گزارش",
          value: "thisYear_RevenueFromFacility"
        }
      ],
      headersdeposit: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        {
          text: "شرکت گزارش دهنده",
          value: "reported_firm"
        },
        {
          text: "عنوان",
          value: "title"
        },
        {
          text: "مانده اول دوره سپرده های سرمایه گذاری",
          value: "StartPeriod_Deposits"
        },
        {
          text: "اصلاحات",
          value: "StartPeriod_Deposits_modifications"
        },
        {
          text: "مانده اول دوره سپرده های سرمایه گذاری- اصلاح شده",
          value: "StartPeriod_Deposits_modified"
        },
        {
          text: "سپرده های دریافتی طی دوره",
          value: "thisPeriod_IncomingDeposit"
        },
        {
          text: "سپرده های تسویه شده طی دوره",
          value: "thisPeriod_setteledDeposits"
        },
        {
          text: "مانده سپرده های سرمایه گذاری پایان دوره",
          value: "EndPeriod_Deposits"
        },
        {
          text: "سود سپرده های سرمایه گذاری از ابتدای سال تا ابتدای دوره",
          value: "PreviousPeriods_InterestOnDeposits"
        },
        {
          text: "اصلاحات",
          value: "PreviousPeriods_InterestOnDeposits_modifications"
        },
        {
          text:
            "سود سپرده های سرمایه گذاری از ابتدای سال تا ابتدای دوره -اصلاح شده",
          value: "PreviousPeriods_InterestOnDeposits_modified"
        },
        {
          text: " سود سپرده های سرمایه گذاری طی دوره گزارش",
          value: "thisPeriod_InterestOnDeposits"
        },
        {
          text:
            "جمع سود سپرده سرمایه گذاری از ابتدای سال مالی تا پایان دوره گزارش",
          value: "Total_InterestOnDeposits"
        }
      ],
      heaadersInsurance: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        {
          text: "شرکت گزارش دهنده",
          value: "reported_firm"
        },
        {
          text: "عنوان",
          value: "title"
        },
        {
          text: "رشته بیمه ای",
          value: "InsuranceField"
        },
        {
          text: "حق بیمه صادره از ابتدای سال تا ابتدای دوره - مبلغ",
          value: "PreviousPeriods_IssuedInsurance_Amount"
        },
        {
          text: "حق بیمه صادره از ابتدای سال تا ابتدای دوره- سهم (درصد)",
          value: "PreviousPeriods_IssuedInusrance_Share"
        },
        {
          text: "خسارت پرداختی از ابتدای سال تا ابتدای دوره - مبلغ",
          value: "PreviousPeriods_DamageRepaid_Amount"
        },
        {
          text: "خسارت پرداختی از ابتدای سال تا ابتدای دوره-سهم (درصد)",
          value: "PreviousPeriods_DamageRepaid_Amount"
        },
        {
          text: "اصلاحات حق بیمه صادره - تا ابتدای دوره - مبلغ",
          value: "Modification_IssuedInsurance_Amount"
        },
        {
          text: "اصلاحات خسارت پرداختی تا ابتدای دوره -مبلغ",
          value: "Modification_DamageRepaid_Amount"
        },
        {
          text: "حق بیمه صادره اصلاح شده -تا ابتدای دوره-مبلغ",
          value: "PreviousModified_IssuedInsurance_Amount"
        },
        {
          text: "حق بیمه صادره اصلاح شده تا ابتدای دوره-درصد",
          value: "PreviousModified_IssuedInusrance_Share"
        },
        {
          text: "خسارت پرداختی اصلاح شده تا ابتدای دوره -مبلغ",
          value: "PreviousModified_DamageRepaid_Amount"
        },
        {
          text: "خسارت پرداختی اصلاح شده تا ابتدای دوره - سهم",
          value: "PreviousModified_DamageRepaid_Share"
        },
        {
          text: "حق بیمه صادره دوره - مبلغ",
          value: "ThisPeriod_IssuedInsurance_Amount"
        },
        {
          text: "حق بیمه صادره دوره - سهم",
          value: "ThisPeriod_IssuedInusrance_Share"
        },
        {
          text: "خسارت پرداختی دوره -مبلغ",
          value: "ThisPeriod_DamageRepaid_Amount"
        },
        {
          text: "خسارت پرداختی دوره -درصد",
          value: "ThisPeriod_DamageRepaid_Share"
        },
        {
          text: "حق بیمه صادره کل سال - مبلغ",
          value: "Total_IssuedInsurance_Amount"
        },
        {
          text: "حق بیمه صادره کل سال -سهم",
          value: "Total_IssuedInusrance_Share"
        },
        {
          text: "خسارت پرداختی کل سال -مبلغ",
          value: "Total_DamageRepaid_Amount"
        },
        {
          text: "خسارت پرداختی کل سال -درصد",
          value: "Total_DamageRepaid_Share"
        }
      ],
      headersconstructionSold: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        {
          text: "شرکت گزارش دهنده",
          value: "reported_firm"
        },
        {
          text: "عنوان پروژه",
          value: "projectName"
        },
        {
          text: "موقعیت پروژه",
          value: "Location"
        },
        {
          text: "نوع پروژه",
          value: "typeOfProject"
        },
        {
          text: "واحد",
          value: "projectUnit"
        },
        {
          text: "بهای تمام شده فروش در ماه جاری",
          value: "thisMonth_Cost"
        },
        {
          text: "متراژ فروش ماه جاری",
          value: "thisMonth_MeterSold"
        },
        {
          text: "نرخ فروش در ماه جاری",
          value: "thisMonth_SaleRate"
        },
        {
          text: "مبلغ فروش ماه جاری",
          value: "thisMonth_SaleAmount"
        },
        {
          text: "بهای تمام شده شناسایی شده ",
          value: "FromBefore_Cost"
        },
        {
          text: "درآمد شناسایی شده",
          value: "FromBefore_Revenue"
        },
        {
          text: "بهای تمام شده از ابتدای سال مالی تا پایان دوره",
          value: "TotalYear_Cost"
        },
        {
          text: "متراژ فروش کل سال",
          value: "TotalYear_MeterSold"
        },
        {
          text: "نرخ فروش کل سال",
          value: "TotalYear_SaleRate"
        },
        {
          text: "مبلغ فروش",
          value: "TotalYear_SaleAmount"
        }
      ],
      headersconstructionOngoing: [
        {
          text: "منتهی به",
          value: "toDate"
        },
        {
          text: "شرکت گزارش دهنده",
          value: "reported_firm"
        },
        {
          text: "عنوان پروژه",
          value: "projectName"
        },
        {
          text: "موقعیت پروژه",
          value: "Location"
        },
        {
          text: "نوع پروژه",
          value: "typeOfProject"
        },
        {
          text: "درصد مالکیت",
          value: "Ownership"
        },
        {
          text: "واحد",
          value: "projectUnit"
        },
        {
          text: "زیر بنای مفید",
          value: "NetMeter"
        },
        {
          text: "درصد پیشرفت فیزیکی در انتهای ماه قبل",
          value: "lastMonth_physicalProgress"
        },
        {
          text: "مبلغ بهای تمام شده در انتهای ماه قبل",
          value: "lastMonth_Cost"
        },
        {
          text: "برآورد هزینه های مانده در انتهای ماه قبل",
          value: "lastMonth_EstimationOfRemainingCost"
        },
        {
          text: "مبلغ بهای تمام شده برآوردی در انتهای ماه قبل",
          value: "lastMonth_EstmiatedTotalCost"
        },
        {
          text: "متراژ پروژه های فروش رفته در طی ماه",
          value: "SoldProjectsDuringMonth_meter"
        },
        {
          text: "بهای تمام شده پروژه های فروش رفته طی ماه",
          value: "SoldProjectsDuringMonth_cost"
        },
        {
          text: "درصد پیشرفت فیزیکی در پایان ماه",
          value: "thisMonth_physicalProgress"
        },
        {
          text: "بهای تمام شده در پایان ماه",
          value: "thisMonth_cost"
        },
        {
          text: "برآورد هزینه های تکمیل در پایان ماه",
          value: "thisMonth_EstimationRemainingCost"
        },
        {
          text: "مبلغ بهای تمام شده برآوردی در پایان ماه",
          value: "thisMonth_EsitmatedTotalCost"
        }
      ],
      DataItems2: [],
      DataItems3: []
    };
  },
  computed: {
    ...mapGetters(["layoutConfig"]),
    filteredItems() {
      return this.DataItems2.filter(item => {
        return item.toDate == this.selectedMonth;
      });
    },
    filteredItems2() {
      return this.DataItems3.filter(item => {
        return item.toDate == this.selectedMonth;
      });
    }
  },
  methods: {
    populateData() {
      this.DataItems2 = this.notices;
      this.DataItems3 = this.deposits;
    },
    gettabs() {
      var lookup = {};
      var lookup2 = {};
      var items = this.DataItems2;
      var result = [];
      var result2 = [];
      var counter = 0;
      for (var item, i = 0; (item = items[i++]); ) {
        var name = item.toDate;
        if (!(name in lookup)) {
          lookup[name] = 1;
          var itemOne = {};
          itemOne["key"] = counter;
          itemOne["value"] = name;
          result.push(itemOne);
          counter += 1;
        }
        if (!(name.split("/")[0] in lookup2)) {
          lookup2[name.split("/")[0]] = 1;
          var itemTwo = {};
          itemTwo["key"] = counter;
          itemTwo["value"] = name.split("/")[0];
          result2.push(itemTwo);
          counter += 1;
        }
      }
      this.todates = result;
      this.todatesyears = result2;
      this.fillNewestMonth();
    },
    getOnesfromthisyear() {
      var lookup = {};
      var items = this.DataItems2;
      var result = [];
      var counter = 0;
      for (var item, i = 0; (item = items[i++]); ) {
        var name = item.toDate;
        if (name.split("/")[0] == this.selectedYear && !(name in lookup)) {
          lookup[name] = 1;
          var itemOne = {};
          itemOne["key"] = counter;
          itemOne["value"] = name;
          result.push(itemOne);
          counter += 1;
        }
      }
      this.todates = result;
      // console.log(result);
      // console.log(this.selectedYear);
    },
    GetFiltered(selectedItem) {
      //   return this.DataItems2.filter(d => {
      //     return Object.keys(this.filters).every(f => {
      //       return this.filters[f].length < 1 || this.filters[f].includes(d[f]);
      //     });
      //   });
      this.selectedMonth = selectedItem;
    },
    GetFilteredYearly(selectedItem) {
      //   return this.DataItems2.filter(d => {
      //     return Object.keys(this.filters).every(f => {
      //       return this.filters[f].length < 1 || this.filters[f].includes(d[f]);
      //     });
      //   });

      this.selectedYear = selectedItem;
    },
    fillNewestMonth() {
      //   console.log(this.todates[0][0]);
      this.selectedMonth = this.todates[0].value;
      this.selectedYear = this.todatesyears[0].value;
    },
    SetNewPagefirstMonth() {
      //   console.log(this.todates[0][0]);
      this.selectedMonth = this.todates[0].value;
      // this.selectedYear = this.todatesyears[0].value;
    },
    setType() {
      this.type = this.typeOf;
      console.log(this.type);
    }
  },
  mounted() {
    this.populateData();
    this.setType();
  },
  watch: {
    notices() {
      //   console.log("Watcher");
      this.populateData();
      this.gettabs();
      this.getOnesfromthisyear();
      this.loading = false;
      // console.log(this.notices);
    },
    deposits() {
      //   console.log("Watcher");
      this.populateData();
      this.gettabs();
      this.getOnesfromthisyear();

      // console.log(this.notices);
    },
    selectedYear: function() {
      this.getOnesfromthisyear();
      this.SetNewPagefirstMonth();
    },
    typeOf() {
      this.setType();
    }
  }
};
</script>
<style scoped>
.FinancialStrength {
  direction: rtl;
  text-align: right;
}
.rtl_centerd {
  direction: rtl;
  text-align: center;
}
.ltr_aligned {
  direction: ltr !important;
  text-align: left;
}
.valign * {
  vertical-align: middle;
}
.redItem {
  color: #ef5350 !important;
}
.greenItem {
  color: #088a2f93 !important;
}
.titleHeaders {
  padding: 5px;
  font-size: 1em;
  text-align: right;
}
.titleHeaders-smaller {
  padding: 1px;
  font-size: 0.9em;
  text-align: right;
}
</style>
