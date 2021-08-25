<template>
  <div class="elements">
    <the-front-logo></the-front-logo>
    <the-front-login></the-front-login>
    </div>
  </div>
</template>

<script>
import TheFrontLogo from "./TheFrontLogo.vue"
import TheFrontLogin from "./TheFrontLogin.vue"

export default {
  components:{
    TheFrontLogo,
    TheFrontLogin
  }
};
</script>

<style scoped>


.elements {
  width: 100vw;
  height: 100vh;
  background-image: url("./../assets/img/bg.jpg");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}

</style>
