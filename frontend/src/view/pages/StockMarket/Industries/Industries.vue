<template>
  <div>
    <div class="row">
      <marquee-text
        class="tickerTape"
        reverse
        :repeat="5"
        :duration="30"
        :paused="paused"
      >
        <div
          class="row"
          style="background-color: #27273b;"
          @mouseenter="paused = !paused"
          @mouseleave="paused = false"
        >
          <div
            v-for="item in this.TickerTape"
            :key="item.ticker"
            class=" mr-4 "
          >
            <div
              class="mr-2 pt-2 pb-2"
              style="height: 100% overflow: hidden; 
    text-align: center; direction:rtl"
            >
              <span class="tickerTapeTicker mr-1 ml-1">
                {{ item.ticker }}
              </span>
              <span class="tickerTapeClose">
                {{ item.close }}
              </span>
              <!-- <v-chip label :style="`background-color:${item.Change} > ${0} ? 'green' : 'red'`">{{ item.Change }}</v-chip> -->
              <v-chip
                label
                v-bind:class="[item.Change > 0 ? 'greenItem' : 'redItem']"
                >{{ item.Change }}%</v-chip
              >
            </div>

            <!-- <v-chip label small class="mr-2">

            </v-chip> -->
          </div>
        </div>
        <!-- <p class="mr-2" v-for="item in this.TickerTape" :key="item.ticker"> <span label class="tickerTapeText">{{ item.ticker }}</span></p> -->
      </marquee-text>
      <div class="col-xxl-4 col-md-6 mb-4">
        <v-card>
          <v-card-title>ارزش بازار صنایع</v-card-title>
          <ApexChart
            v-if="Pieseries.length"
            type="pie"
            height="200%"
            width="100%"
            :series="Pieseries"
            :chartOptions="PiechartOptions"
          />
        </v-card>
      </div>

      <div class="col-xxl-6 col-md-6 mb-4">
        <v-card>
          <v-card-title>برترین گروه های صنعت</v-card-title>
          <ApexChart
            v-if="Barseries.length"
            type="bar"
            height="200%"
            width="100%"
            :series="Barseries"
            :chartOptions="BarchartOptions"
          />
        </v-card>
      </div>
      <div class="col-xxl-6 col-md-6 mb-4">
        <v-card>
          <v-card-title>تاثیر صنایع در شاخص</v-card-title>
          <ApexChart
            type="bar"
            width="100%"
            :series="EffectOnIndexSeries"
            :chartOptions="EffectOnIndexOptions"
          />
        </v-card>
      </div>
      <div class="col-xxl-6 col-md-6 mb-4">
        <v-card>
          <v-card-title>ورود و خروج حقیقی به صنایع</v-card-title>
          <ApexChart
            type="bar"
            width="100%"
            height="200%"
            :series="HHseries"
            :chartOptions="HHoptions"
          />
        </v-card>
      </div>
      <div class="col-xxl-6 col-md-6">
        <v-card>
          <v-card-title>ورود و خروج حقیقی به صنایع</v-card-title>
          <ApexChart
            type="bar"
            width="100%"
            height="200%"
            :series="test"
            :chartOptions="testOptions"
          />
        </v-card>
      </div>
      <div class="col-xxl-8 col-md-8">
        <v-card>
          <v-card-title
            >بار چارت افقی با تایم فریم برای بازدهی صنایع</v-card-title
          >
          <div class="mr-5">
            <span>بازه زمانی:</span>
            <b-button-group>
              <b-button class="mr-1" pill variant="outline-primary"
                >ماه</b-button
              >
              <b-button class="mr-1" pill variant="outline-primary"
                >۳ ماه</b-button
              >
              <b-button class="mr-1" pill variant="outline-primary"
                >۶ ماه</b-button
              >
              <b-button class="mr-1" pill variant="outline-primary"
                >سال</b-button
              >
              <b-button class="mr-1" pill variant="outline-primary"
                >۳ سال</b-button
              >
              <b-button class="mr-1" pill variant="outline-primary"
                >کل</b-button
              >
            </b-button-group>
            <!-- <v-btn
              id="fi"
              class="ml-1"
              outlined
              dark
              small
              color="#136bf7"
              @click="changeTimeFrame"
              >ماه</v-btn
            >
            <v-btn
              class="ml-1"
              dark
              small
              color="#136bf7"
              @click="changeTimeFrame"
              >۳ ماه</v-btn
            >
            <v-btn
              class="ml-1"
              dark
              small
              color="#136bf7"
              @click="changeTimeFrame"
              >۶ ماه</v-btn
            >
            <v-btn
              class="ml-1"
              dark
              small
              color="#136bf7"
              @click="changeTimeFrame"
              >سال</v-btn
            >
            <v-btn
              class="ml-1"
              dark
              small
              color="#136bf7"
              @click="changeTimeFrame"
              >۳ سال</v-btn
            >
            <v-btn
              class="ml-1"
              dark
              small
              color="#136bf7"
              @click="changeTimeFrame"
              >کل</v-btn
            > -->
          </div>

          <ApexChart
            type="bar"
            width="100%"
            height="500%"
            :series="ReturnSeries"
            :chartOptions="ReturnOptions"
          />
        </v-card>
      </div>
      <div class="col-xxl-4 col-md-4">
        <v-tabs>
          <v-tab>بهترین</v-tab>
          <v-tab>بدترین</v-tab>
          <v-tab-item><IndustryTechnicalBest /></v-tab-item>
          <v-tab-item><IndustryTechnicalWorse /></v-tab-item>
        </v-tabs>
      </div>
    </div>
  </div>
</template>
<script>
// import ErrorMine from "@/view/pages/error/Error-6.vue";
import MarqueeText from "vue-marquee-text-component";

import ApexChart from "@/view/content/charts/ApexChart";
import IndustryTechnicalBest from "@/view/pages/StockMarket/Industries/Content/IndustryTechnical‌Best";
import IndustryTechnicalWorse from "@/view/pages/StockMarket/Industries/Content/IndustryTechnicalWorse";
// import axios from "axios";
export default {
  name: "Industries",
  components: {
    ApexChart,
    IndustryTechnicalBest,
    IndustryTechnicalWorse,
    MarqueeText
    // Error,
    // ErrorMine
  },
  data() {
    return {
      paused: false,
      TickerTape: [],
      ReturnSeries: [
        {
          // name: "Marine Sprite",
          data: [
            400,
            390,
            386,
            378,
            375,
            364,
            355,
            341,
            337,
            332,
            323,
            321,
            286,
            278,
            275,
            264,
            255,
            241,
            237,
            232,
            223,
            221,
            186,
            178,
            175,
            164,
            155,
            141,
            137,
            132,
            123,
            121,
            86,
            78,
            75,
            64,
            55,
            41,
            37,
            32,
            23,
            21
          ]
        }
      ],
      ReturnOptions: {
        chart: {
          type: "bar",
          height: 350,
          toolbar: {
            show: false
          }
        },
        legend: {
          show: false
        },
        plotOptions: {
          bar: {
            horizontal: true,
            distributed: true,
            barHeight: "100%",
            dataLabels: {
              position: "bottom"
            }
          }
        },
        dataLabels: {
          enabled: true,
          textAnchor: "start",
          style: {
            colors: ["#fff"]
          },
          formatter: function(val, opt) {
            return opt.w.globals.labels[opt.dataPointIndex] + ":  " + val;
          }
        },
        xaxis: {
          categories: [
            "29-ماشین آلات",
            "23-فراورده نفتی",
            "13-کانه فلزی",
            "54-کانی غیرفلزی",
            "42-غذایی بجز قند",
            "73-اطلاعات و ارتباطات",
            "10-ذغال سنگ",
            "34-خودرو",
            "38-قند و شکر",
            "60-حمل و نقل",
            "32-وسایل ارتباطی",
            "58-سایرمالی",
            "22-انتشار و چاپ",
            "27-فلزات اساسی",
            "44-شیمیایی",
            "31-دستگاههای برقی",
            "56-سرمایه گذاریها",
            "01-زراعت",
            "25-لاستیک",
            "39-چند رشته ای ص",
            "64-رادیویی",
            "20-محصولات چوبی",
            "بیمه و بازنشسته66",
            "17-منسوجات",
            "33-ابزار پزشکی",
            "67-اداره بازارهای مالی",
            "14-سایر معادن",
            "استخراجنفتجزکشف11",
            "47خرده فروشی به جز وسایل نقلیه",
            "19-محصولات چرمی",
            "53-سیمان",
            "57-بانکها",
            "21-محصولات کاغذ",
            "شاخص صنعت",
            "74-فنی مهندسی",
            "40-تامین آب، برق، گاز",
            "49-کاشی و سرامیک",
            "28-محصولات فلزی",
            "43-مواد دارویی",
            "70-انبوه سازی",
            "72-رایانه"
          ],
          labels: {
            formatter: function(val) {
              return val + "K";
            }
          }
        },
        yaxis: {
          title: {
            text: undefined
          }
        },
        tooltip: {
          y: {
            formatter: function(val) {
              return val + "K";
            }
          }
        },
        fill: {
          opacity: 1
        }
      },
      test: [
        {
          data: [
            1.4,
            2,
            2.2,
            2.5,
            2.8,
            3,
            3.8,
            4.6,
            2,
            2.2,
            2.5,
            2.8,
            3,
            3.8,
            4.6,
            2,
            2.2,
            2.5,
            2.8,
            3,
            3.8,
            4.6
          ]
        },
        {
          data: [
            -2.0,
            -2.9,
            -3.7,
            -3.6,
            -4.4,
            -4.5,
            -4.8,
            -5,
            -2.9,
            -3.7,
            -3.6,
            -4.4,
            -4.5,
            -4.8,
            -5,
            -2.9,
            -3.7,
            -3.6,
            -4.4,
            -4.5,
            -4.8,
            -5
          ]
        }
      ],
      testOptions: {
        chart: {
          type: "bar",
          height: 440,
          stacked: true,
          toolbar: {
            show: false
          }
        },
        colors: ["#008FFB", "#FF4560"],
        plotOptions: {
          bar: {
            horizontal: true,
            barHeight: "100%",
            dataLabels: {
              position: "top"
            }
          }
        },
        dataLabels: {
          enabled: true
        },
        stroke: {
          width: 0,
          colors: ["#fff"]
        },

        grid: {
          xaxis: {
            tickPlacement: "on",
            lines: {
              show: false
            }
          }
        },
        yaxis: {
          min: -10,
          max: 10,
          title: {
            // text: 'Age',
          },
          tickPlacement: "on"
        },
        tooltip: {
          shared: false,
          x: {
            formatter: function(val) {
              return val;
            }
          },
          y: {
            formatter: function(val) {
              return Math.abs(val) + "%";
            }
          }
        },
        xaxis: {
          categories: [
            "85+",
            "80-84",
            "75-79",
            "70-74",
            "65-69",
            "60-64",
            "55-59",
            "50-54"
          ]
        }
      },
      Pieseries: [],
      Barseries: [],

      HHseries: [
        {
          name: "Males",
          data: [
            5.4,
            4.65,
            3.76,
            2.88,
            2.5,
            2.1,
            2,
            1.8,
            -4,
            -4.4,
            -4.3,
            -4.2,
            -4,
            -3,
            -2.5,
            -1
          ]
        }
      ],
      HHoptions: {
        chart: {
          type: "bar",
          height: 100,
          stacked: true
        },
        // colors: ["#16f222", "#FF4560"],
        colors: [
          function({ value }) {
            if (value > 0) {
              return "#36eb0e";
            } else {
              return "#D9534F";
            }
          }
        ],
        plotOptions: {
          bar: {
            horizontal: false,
            barHeight: "80%"
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          width: 1,
          colors: ["#fff"]
        },
        grid: {
          xaxis: {
            lines: {
              show: true
            }
          }
        },
        yaxis: {
          min: -5,
          max: 5,
          title: {
            // text: 'Age',
          }
        },
        tooltip: {
          shared: false,
          x: {
            formatter: function(val) {
              return val;
            }
          },
          y: {
            formatter: function(val) {
              return Math.abs(val) + "%";
            }
          }
        },
        // title: {
        //   text: "Mauritius population pyramid 2011"
        // },
        xaxis: {
          categories: [
            "85+",
            "80-84",
            "75-79",
            "70-74",
            "65-69",
            "60-64",
            "55-59",
            "50-54",
            "45-49",
            "40-44",
            "35-39",
            "30-34",
            "25-29",
            "20-24",
            "15-19",
            "10-14",
            "5-9",
            "0-4"
          ],
          title: {
            text: "Percent"
          },
          labels: {
            formatter: function(val) {
              return Math.abs(Math.round(val)) + "%";
            }
          }
        }
      },

      EffectOnIndexSeries: [
        {
          data: [
            44,
            55,
            41,
            64,
            22,
            43,
            -21,
            -32,
            -42,
            -45,
            -56,
            -12,
            41,
            64,
            22,
            43,
            -21,
            -32,
            -42,
            -45,
            -56,
            -12,
            41,
            64,
            22,
            43,
            -21,
            -32,
            -42,
            -45,
            -56,
            -12,
            41,
            64,
            22,
            43,
            -21,
            -32,
            -42,
            -45,
            -56,
            -12
          ]
        }
      ],
      EffectOnIndexOptions: {
        chart: {
          type: "bar",
          height: 50,
          toolbar: {
            show: true
          }
        },
        plotOptions: {
          bar: {
            horizontal: false,
            barHeight: "100%",
            distributed: true
          }
        },

        dataLabels: {
          enabled: true,

          style: {
            fontSize: "7px",
            colors: ["#fff"]
          }
        },
        labels: {
          show: true
        },
        xaxis: {
          categories: [
            "South Korea",
            "Canada",
            "United Kingdom",
            "Netherlands",
            "Italy",
            "France",
            "Japan",
            "United States",
            "China",
            "Germany"
          ],
          labels: {
            show: true
          },
          offsetX: 109,
          offsetY: 500
        }
      },
      BarchartOptions: {
        chart: {
          type: "bar",
          height: 350,
          toolbar: {
            show: false
          },
          fontFamily: "Vazir"
        },
        legend: {
          show: false
        },
        plotOptions: {
          bar: {
            horizontal: true,
            barHeight: "100%",
            distributed: true
          }
        },
        colors: ["#33b2df", "#546E7A", "#d4526e", "#13d8aa", "#A5978B"],
        dataLabels: {
          enabled: true,

          style: {
            colors: ["#fff"]
          }
        },
        xaxis: {
          categories: [
            "South Korea",
            "Canada",
            "United Kingdom",
            "Netherlands",
            "Italy",
            "France",
            "Japan",
            "United States",
            "China",
            "Germany"
          ],
          labels: {
            show: true
          },
          offsetX: 109,
          offsetY: 500
        }
      },
      PiechartOptions: {
        chart: {
          width: 400,
          height: 350,
          type: "pie",
          fontFamily: "Vazir",
          animations: {
            enabled: false
          },
          events: {
            // legendClick: function(chartContext, seriesIndex, config) {
            //   // console.log(chartContext);
            //   // console.log(seriesIndex);
            //   // console.log(config);
            // },
            dataPointSelection: (event, chartContext, config) => {
              // console.log(chartContext);
              // console.log(event);
              // console.log(config);
              this.testing(config.dataPointIndex);
            }
          }
        },
        legend: {
          // show: false,
          fontSize: 10,
          fontFamily: "Vazir"
          // position: "bottom"
        },
        labels: [],
        responsive: [
          {
            breakpoint: 480,
            options: {
              chart: {
                width: 200
              }
            }
          }
        ]
      }
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    testing(seriesIndex) {
      // console.log(this.PiechartOptions.labels[seriesIndex]);
      // console.log(this.Pieseries[seriesIndex]);
      // this.PiechartOptions.labels = persianNames;
      // console.log(this.chartOptions.labels);

      // this.Pieseries = marketCaps;
      this.$router.push({
        name: "IndustriesDetail",
        params: { id: seriesIndex }
      });
    },
    changeTimeFrame() {
      this.ReturnSeries = [
        { data: [123, 121, 110, 100, 98, 90, 76, 68, 61, 57, 43] }
      ];
      document.getElementById("fi").style.color = "red !important";
    },
    index() {
      this.$router.push({ name: "IndustriesDetail", params: { id: 2 } });
    },
    loadData() {
      // eslint-disable-next-line no-unused-vars
      this.getTickerTapeData().then(response => {
        this.getPieChartData();
      });
    },
    async getPieChartData() {
      await this.axios.get("/api/IndexMarketCap").then(responsive => {
        let data = responsive.data;
        let persianNames = [];
        let marketCaps = [];
        let itemValue = [];
        for (let item of data) {
          // console.log(item);
          persianNames.push(item.persianName);
          marketCaps.push(item.marketCap);
          itemValue.push({ name: item.persianName, value: item.Value });
        }
        // console.log(persianNames);
        this.PiechartOptions.labels = persianNames;
        // console.log(this.chartOptions.labels);

        this.Pieseries = marketCaps;
        itemValue.sort(this.compareValues("value", "desc"));
        itemValue = itemValue.slice(0, 6);
        // console.log(itemValue);
        let names = [];
        let values = [];
        for (let item of itemValue) {
          names.push(item.name);
          values.push(item.value);
        }

        this.Barseries = [{ data: values }];
        this.BarchartOptions.xaxis.categories = names;
      });
    },
    async getTickerTapeData() {
      await this.axios
        .get("/api/TickerTape")
        .then(response => {
          let data = response.data;
          this.TickerTape = data;
          // this.TickerTape.pop();
        })
        .catch(error => {
          console.log(error);
        });
    },
    compareValues(key, order = "asc") {
      return function innerSort(a, b) {
        if (!a.hasOwnProperty(key) || !b.hasOwnProperty(key)) {
          // property doesn't exist on either object
          return 0;
        }

        const varA = typeof a[key] === "string" ? a[key].toUpperCase() : a[key];
        const varB = typeof b[key] === "string" ? b[key].toUpperCase() : b[key];

        let comparison = 0;
        if (varA > varB) {
          comparison = 1;
        } else if (varA < varB) {
          comparison = -1;
        }
        return order === "desc" ? comparison * -1 : comparison;
      };
    }
  }
};
</script>
<style scoped>
@import "~bootstrap/dist/css/bootstrap.css";
#fi {
  color: red !important;
}
.tickerTape {
  direction: ltr;
  background-color: tickerTape;
}
.tickerTapeTicker {
  color: aliceblue;
}
.tickerTapeClose {
  color: aliceblue;
  font-size: 0.8rem;
}
.v-chip.v-size--default {
  font-size: 0.7rem;
  height: 1.8em;
  direction: ltr;
  padding-right: 0.8em;
  padding-left: 0.8em;
}
.redItem {
  color: aliceblue;
  background-color: red !important;
}
.greenItem {
  color: aliceblue;
  background-color: green !important;
}
.apexcharts-text tspan {
  font-family: "Vazir";
}
</style>
