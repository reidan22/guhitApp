import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);
import UserPage from "./components/pages/UserPage.vue";
import GuhitFeed from "./components/pages/GuhitFeed.vue";
import ImagePage from "./components/pages/ImagePage.vue";

const routes = [
  { path: "/", component: UserPage },
  { path: "/feed", component: GuhitFeed },
  { path: "/user", component: UserPage },
  { path: "/image/:id", component: ImagePage, props: true },
];
const router = new VueRouter({
  mode: "history",
  routes,
});

export default router;
