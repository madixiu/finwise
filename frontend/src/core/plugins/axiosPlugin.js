import axios from "axios";
import VueAxios from "vue-axios";
export default {
  install(Vue) {
    axios.defaults.baseURL = "http://45.82.136.21";
    // axios.defaults.baseURL = "http://localhost";
    Vue.use(VueAxios, axios);
  }
};
