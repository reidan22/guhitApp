<template>
  <div class="img__page">
    <div class="container-fluid">
      <div class="row">
        <div class="col-8">
          <div class="row">
            <h2>{{ image.title }} by {{ image.user_id }}</h2>
          </div>
          <div class="row img">
            <img :src="getImgUrl(image.image_file)" alt="Art file." />
          </div>
          <div class="row">
            <p>{{ image.caption }}</p>
          </div>
        </div>
        <comments-view :photo="image"></comments-view>
      </div>
    </div>
  </div>
</template>

<script>
import CommentsView from "../CommentsView.vue";
export default {
  components: {
    CommentsView,
  },
  methods: {
    getImgUrl(pic) {
      if (pic) {
        return require("@/static/picture/" + pic);
      }
    },
  },
  computed: {
    image() {
      if (this.images !== null && this.user !== null) {
        return this.$store.state.image;
      }
    },
  },
};
</script>

<style scoped>
p {
}

.row,
.col {
  margin: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}
.img__page {
  background-color: #005b96;
  height: 100vh;
}

img {
  width: auto;
  max-height: 100%;
  border: 0.25rem solid white;
  background: white;
}

.img {
  height: 60vh;
}
h2,
p {
  color: #b3cde0;
  margin-top: 1rem;
}

.comments {
  /* background: red; */
  height: 15rem;
  overflow-y: auto;
}
</style>
