<template>
  <div class="user__page">
    <guhit-feed-images class="post"></guhit-feed-images>
  </div>
</template>

<script>
import FeedDP from "../FeedDP.vue";
import GuhitFeedImages from "../GuhitFeedImages.vue";
export default {
  components: {
    "feed-dp": FeedDP,
    "guhit-feed-images": GuhitFeedImages,
  },
  created() {},
  methods: {
    getImgUrl(pic) {
      if (pic) {
        return require("@/static/profile_picture/" + pic);
      }
    },
  },
  computed: {
    user() {
      return this.$store.state.user;
    },

    fname() {
      if (this.user) {
        return this.user.fname;
      } else {
        return "Juan";
      }
    },
    lname() {
      if (this.user) {
        return this.user.lname;
      } else {
        return "dela Cruz";
      }
    },
  },
};
</script>

<style scoped>
div {
  margin: 0;
}
.user__page {
  background-color: #005b96;
  height: 100vh;
}

.post {
}
</style>
