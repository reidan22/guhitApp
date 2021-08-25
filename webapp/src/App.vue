<template>
  <div id="app">
    <the-header v-if="isLogin === true"></the-header>
    <the-front-page v-if="isLogin === false"></the-front-page>
    <router-view></router-view>
    <!-- <p class="guhit-logo" @click="changeIsLogin">12345</p> -->
    <!-- <p>{{ flaskGreeting }}</p> -->
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import TheHeader from "./components/TheHeader.vue";
import TheFrontPage from "./components/TheFrontPage.vue";

document.title = "Guhit";

export default {
  name: "App",

  components: {
    HelloWorld,
    TheHeader,
    TheFrontPage,
  },
  data: function() {
    return {
      greeting: "132",
      flaskGreeting: "",
    };
  },
  methods: {
    changeTest: function() {
      this.greeting = "WHAT";
    },
  },
  computed: {
    isLogin() {
      return this.$store.state.isLogin;
    },
  },
  created: async function() {
    setInterval(() => {
      this.$store.commit("getUsers");
      this.$store.commit("getImages");
      this.$store.commit("getComments");
    }, 1000);

    // const gResponse = await fetch("http://localhost:5000/api/users");
    // const gObject = await gResponse.json();
    // // this.flaskGreeting = gObject.greeting;
    // console.log(gObject);
  },
  updated: async function() {
    this.$store.commit("getUsers");
    this.$store.commit("getImages");
    this.$store.commit("getComments");

    // const gResponse = await fetch("http://localhost:5000/api/users");
    // const gObject = await gResponse.json();
    // // this.flaskGreeting = gObject.greeting;
    // console.log(gObject);
  },
  mount() {
    setInterval(() => {
      this.$store.commit("getUsers");
      this.$store.commit("getImages");
      this.$store.commit("getComments");
    }, 2500);
  },
};
</script>

<style>
@font-face {
  font-family: "Brushes";
  src: url("./assets/fonts/BrushKing-MVVPp.otf");
}
#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  font-family: "Roboto", sans-serif;
  color: #011f4b;
  font-size: 2vw;
  /* background-color: #292d30; */
  /* overflow: hidden; */
}

body {
  overflow: hidden;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
}

.drop__shadow {
  box-shadow: 0 2px 8px #005b96;
}

.round__border {
  border-radius: 25px;
}
/* #011f4b • #03396c • #005b96 • #6497b1 • #b3cde0*/
</style>
