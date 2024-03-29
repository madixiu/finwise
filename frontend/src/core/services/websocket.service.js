import Vue from "vue";
// import store from "../store";

// let vm = this
let URI = "localhost:8000";
// let URI = "45.82.136.21"

const WsService = {
  init() {
    try {
      // const option_ws = new WebSocket('45.82.136.21:9000/ws/')
      let MostViewed = new WebSocket("ws://" + URI + "/ws/Top5Views");
      let ImpactOnIndex = new WebSocket("ws://" + URI + "/ws/ImpactOnIndex");
      let highestVolume = new WebSocket("ws://" + URI + "/ws/HighestVolume");
      let HighestValue = new WebSocket("ws://" + URI + "/ws/HighestValues");
      let highestSupply = new WebSocket("ws://" + URI + "/ws/HighestSupplies");
      let highestDemand = new WebSocket("ws://" + URI + "/ws/HighestDemands");

      // const option_ws2 = new WebSocket('ws://45.82.136.21/ws/test')
      Vue.prototype.$socketMostViewed = MostViewed;
      Vue.prototype.$socketImpactOnIndex = ImpactOnIndex;
      Vue.prototype.$socketMarketHighestDemands = highestDemand;
      Vue.prototype.$socketMarketHighestSupplies = highestSupply;
      Vue.prototype.$socketMarketHighestTVolumes = HighestValue;
      Vue.prototype.$socketMarketHighestTValues = highestVolume;

      // option_ws.onopen = (event) => console.log('ws connected' + event)

      // define store dispatch here -------------
      // store.dispatch("setSocketOpen");
      // store.dispatch('websocketIndex/setSocketOpen')
    } catch (error) {
      console.log("error in websocket:" + error);
    }
  }
};

export default WsService;
