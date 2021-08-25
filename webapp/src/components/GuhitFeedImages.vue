<template>
  <div class="all">
    <span class="img" v-for="image in reverseImgOrder">
      <router-link :to="`/image/` + image.id">
        <img
          @click="passImage(image)"
          :src="getImgUrl(image.image_file)"
          alt="Image file."
        />
      </router-link>
      <!-- <guhit-feed-comments :imageID="image.id"></guhit-feed-comments> -->
      <comments-view :photo="image"></comments-view>
    </span>
  </div>
</template>

<script>
import GuhitFeedComments from "./GuhitFeedComments.vue";
import CommentsView from "./CommentsView.vue";

export default {
  components: {
    "guhit-feed-comments": GuhitFeedComments,
    "comments-view": CommentsView,
  },
  methods: {
    getImgUrl(pic) {
      if (pic) {
        return require("@/static/picture/" + pic);
      }
    },
    passImage(image) {
      this.$store.commit("getImage", image);
    },
  },
  computed: {
    reverseImgOrder() {
      return this.images.reverse();
    },
    images() {
      return this.$store.state.images;
    },
    user() {
      return this.$store.state.user;
    },
    filterImages() {
      if (this.images !== null && this.user !== null) {
        return this.images.filter((el) => el.user_id === this.user.user_id);
      }
    },
  },
};
</script>

<style scoped>
.all {
  height: 20rem;
  overflow-y: auto;
  overflow-x: none;
}

img {
  border: 0.25rem solid white;
  height: auto;
  width: 30rem;
  margin: 0.1rem;
  /* transition: 0.25s; */
}

img:hover {
  /* transform: scale(0.95); */
}

.img {
  margin: 0;
  padding: 0;
}
span {
  display: flex;
  align-items: center;
  justify-content: left;
}
</style>
