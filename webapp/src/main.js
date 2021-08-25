import Vue from "vue";
import App from "./App.vue";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import router from "./router.js";
import store from "./store.js";
Vue.config.productionTip = false;

const app = new Vue({
  router,
  store,
  render: function(h) {
    return h(App);
  },
});

app.$mount("#app");
