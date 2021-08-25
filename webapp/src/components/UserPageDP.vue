<template>
  <div>
    <img :src="getImgUrl(user.prof_pic)" alt="User image." />
  </div>
</template>

<script>
export default {
  computed: {
    user() {
      if (this.$store.state.user) {
        return this.$store.state.user;
      } else {
        return { prof_pic: "test.png" };
      }
    },
  },
  methods: {
    getImgUrl(pic) {
      if (pic) {
        return require("@/static/profile_picture/" + pic);
      }
    },
  },
};
</script>

<style scoped>
div {
  display: flex;
  align-items: center;
  justify-content: center;
  /* background: red; */
  width: 10rem;
  height: 10rem;

  /* overflow: hidden; */
}
p {
  font-size: 30px;
}
img {
  object-fit: cover;
  width: 10rem;
  height: 10rem;
  border-radius: 50%;
  border-style: none;
}
</style>
