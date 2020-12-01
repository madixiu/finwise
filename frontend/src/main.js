import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "@/core/services/store";
import WsService from "@/core/services/websocket.service.js";
// import JwtService from "@/core/services/jwt.service";
// import ApiService from "@/core/services/api.service";
// import MockService from "@/core/mock/mock.service";
// import { VERIFY_AUTH } from "@/core/services/store/auth.module";
// import { RESET_LAYOUT_CONFIG } from "@/core/services/store/config.module";
// apollo imports for graphql
import { ApolloClient } from "apollo-client";
import { HttpLink } from "apollo-link-http";
import { InMemoryCache } from "apollo-cache-inmemory";
import { setContext } from "apollo-link-context";
import VueApollo from "vue-apollo";
// vxe-table imports
import "./core/plugins/utils";
import "./core/plugins/table";
// import VXETable from "vxe-table";
// import "vxe-table/lib/style.css";
// import XEUtils from "xe-utils";

// -------------------------
// import ApolloService from "@/core/services/apollo.service";
//vxe-table usage
// Vue.use(VXETable);
// Vue.use(XEUtils);

// HTTP connection to the API graphql/apollo
const httpLink = new HttpLink({
  // You should use an absolute URL here
  uri: "http://localhost:8000/graphql"
});
const authLink = setContext((_, { headers }) => {
  if (store.getters.currentUserAccessToken) {
    var token = store.getters.currentUserAccessToken;
    console.log(store.getters.currentUserAccessToken);
  }

  // return the headers to the context so httpLink can read them
  return {
    headers: {
      ...headers,
      Authorization: token ? `JWT ${token}` : ""
    }
  };
});
// Cache implementation graphql/apollo
const cache = new InMemoryCache();

// Create the apollo client graphql/apollo
const apolloClient = new ApolloClient({
  // link: httpLink,
  link: authLink.concat(httpLink),
  cache
});
// using apollo/graphql
Vue.use(VueApollo);
//-------------------------------

// The provider holds the Apollo client instances that can then be used by all the child components
const apolloProvider = new VueApollo({
  defaultClient: apolloClient
  // loadingKey to ‘loading’ so that we can easily display a loading indicator in the UI
  // defaultOptions: {
  //   $loadingKey: "loading"
  // }
});
// const apolloProvider = ApolloService.init();
Vue.config.productionTip = false;

// Global 3rd party plugins
import "popper.js";
import "tooltip.js";
import PerfectScrollbar from "perfect-scrollbar";
window.PerfectScrollbar = PerfectScrollbar;
import ClipboardJS from "clipboard";
window.ClipboardJS = ClipboardJS;

// Vue 3rd party plugins
import i18n from "@/core/plugins/vue-i18n";
import vuetify from "@/core/plugins/vuetify";
import "@/core/plugins/portal-vue";
import "@/core/plugins/bootstrap-vue";
import "@/core/plugins/perfect-scrollbar";
import "@/core/plugins/highlight-js";
import "@/core/plugins/inline-svg";
import "@/core/plugins/apexcharts";
import "@/core/plugins/metronic";
import "@mdi/font/css/materialdesignicons.css";
import "@/core/plugins/treeselect";
import "@/core/plugins/formvalidation";
// API service init
// ApiService.init();
WsService.init();

// Remove this to disable mock API
// MockService.init();

//crypto JS//
import VueCryptojs from "vue-cryptojs";

Vue.use(VueCryptojs);

// router.beforeEach((to, from, next) => {
// reset config to initial state
// store.dispatch(RESET_LAYOUT_CONFIG);
//   next();
//   router.push({ name: "dashboard" });
//   // Scroll page to top on every route change
//   setTimeout(() => {
//     window.scrollTo(0, 0);
//   }, 100);
// });

new Vue({
  VueCryptojs,
  router,
  store,
  i18n,
  vuetify,
  // injecting apolloProvider here // eslint-disable-next-line
  apolloProvider,
  render: h => h(App)
}).$mount("#app");
