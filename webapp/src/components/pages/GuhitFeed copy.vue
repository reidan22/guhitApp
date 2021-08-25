<template>
  <div class="feed">
    <div class="row dp">
      <!-- <img class="img__dp" :src="getDP(user.prof_pic)" alt="" /> -->DP
    </div>
    <div class="posts">
      <span v-for="image in images">
        {{ getImageOfPost(image) }}
        <div class="row post">
          <div class="col img">
            <!-- {{ getUserOfPost(image.user_id) }} -->
            <img class="img__user" :src="getDP(post_user.prof_pic)" alt="" />
            <router-link :to="`/image/` + image.id">
              <img
                class="img__post"
                @click="passImage(image)"
                :src="getImg(image.image_file)"
                alt="Image file."
              />
            </router-link>
          </div>
          <div class="col comments">
            <div class="row round__border">
              <!-- <span v-for="comment in comments"> -->
              {{ getCommentsofPost(post_image) }}
              <!-- </span> -->
            </div>
          </div>
        </div>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      post_image: null,
      comment_user: null,
    };
  },
  methods: {
    filterComments() {
      if (this.comments !== null && this.user !== null && this.image !== null) {
        return this.comments.filter((el) => el.img_id === this.image.id);
      }
    },
    getCommentsofPost(image) {
      if (this.comments !== null && this.user !== null && this.image !== null) {
        return this.comments.filter((el) => el.image_id === image.id);
      }
    },
    // getUserOfPost(user) {
    //   this.post_user = user;
    // },
    getImageOfPost(image) {
      this.post_image = image;
    },
    passImage(image) {
      this.$store.commit("getImage", image);
    },
    getDP(pic) {
      if (pic && this.user !== null) {
        return require("@/static/profile_picture/" + pic);
      }
    },
    getImg(pic) {
      if (pic && this.user !== null) {
        return require("@/static/picture/" + pic);
      }
    },
  },
  computed: {
    post_user() {
      return this.users.filter((el) => el.user_id === this.post_image.user_id);
    },
    user() {
      return this.$store.state.user;
    },
    users() {
      return this.$store.state.users;
    },
    images() {
      return this.$store.state.images;
    },
    comments() {
      return this.$store.state.comments;
    },
  },
};
</script>

<style scoped>
p {
}
.feed {
  display: block;
  justify-content: center;
  align-items: flex-start;
  background-color: #005b96;
  height: 100vh;
  overflow-y: auto;
}
.post {
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 10rem;
  margin-top: 0.5rem;
}

.row .post {
  display: flex;
}
.dp,
.user__id {
  display: flex;
  justify-content: center;
  align-items: center;
}

span {
  display: flex;
  justify-content: flex-start;
  align-items: center;
}

.img {
  display: flex;
  justify-content: center;
  /* background: red; */
  overflow: hidden;
  padding-left: 5rem;
}

.comments {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  width: 2rem;
  height: 10rem;
  overflow: hidden;
}

.img__dp {
  margin-top: 1rem;
  object-fit: cover;
  width: auto;
  height: 10rem;
  border-radius: 50%;
}

.img__post {
  object-fit: cover;
  width: auto;
  height: 10rem;
}

.img__user {
  object-fit: cover;
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  border-style: none;
  margin-bottom: 0.5rem;
}

.comments .row {
  background: #b3cde0;
}
</style>
