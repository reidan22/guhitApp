import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    sampleName: "Dan Rei 22",
    isLogin: false,
    username: null,
    password: null,
    user: null,
    users: null,
    image: null,
    images: null,
    comments: null,
    comment: null,
    dbProfPic: "./static/profile_picture/",
    dbPic: "./assets/static/picture/",
    userReg: null,
  },
  mutations: {
    changeIsLogin(state) {
      state.isLogin = !state.isLogin;
      // alert(this.isLogin);
    },
    getLoginInfo(state, payload) {
      state.username = payload.username;
      state.password = payload.password;
    },
    async getUsers(state) {
      let gResponse = await fetch("http://127.0.0.1:5000/api/users");
      let gObject = await gResponse.json();
      state.users = gObject;
      // console.log(gObject);
    },
    async getImages(state) {
      let gResponse = await fetch("http://127.0.0.1:5000/api/images");
      let gObject = await gResponse.json();
      state.images = gObject;
    },

    async getComments(state) {
      let gResponse = await fetch("http://localhost:5000/api/comments");
      let gObject = await gResponse.json();
      state.comments = gObject;
    },
    async postUser(load) {
      await fetch("http://127.0.0.1:5000/api/users", {
        method: "POST",
        body: JSON.stringify(load),
        headers: { "Content-type": "application/json; charset=UTF-8" },
      });
      console.log(load);
    },
    async postComment(load) {
      await fetch("http://127.0.0.1:5000/api/comments", {
        method: "POST",
        body: JSON.stringify(load),
        headers: { "Content-type": "application/json; charset=UTF-8" },
      });
      console.log(load);
    },
    getUser(state, user) {
      state.user = user;
    },
    getImage(state, image) {
      state.image = image;
    },
  },
  getters: {
    users: (state) => {
      return state.users;
    },
    images: (state) => {
      return state.images;
    },
    comments: (state) => {
      return state.comments;
    },
  },
});

export default store;
