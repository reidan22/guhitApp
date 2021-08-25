<template>
  <div class="comments">
    <span class="post__comment" v-for="comment in comments">
      <!-- <div class="fluid-container">
        <div class="row">
          <div class="col-2">
            {{ usersFrom(comment) }}
          </div>
          <div class="col-10 comment__box round__border">
            <p>{{ comment.comment_from }}</p>
            {{ comment.comment }}
          </div>
        </div>
      </div> -->
      <div class="row" v-if="image_ID === comment.img_id">
        <div class="fluid-container">
          <div class="row">
            <div class="">
              {{ usersFrom(comment) }}
              <img :src="getImgUrl1(comment_from)" alt="" />
            </div>
            <div class="comment__box round__border">
              <div class="row">
                <p>{{ comment.comment_from }}</p>
              </div>
              <div class="row">
                {{ comment.comment }}
              </div>
            </div>
          </div>
        </div>
      </div>
    </span>
  </div>
</template>

<script>
export default {
  props: ["imageID"],
  data: function() {
    return {
      comment_from: null,
      comment_profpic: null,
      pic_path: null,
      post_comment: null,
    };
  },
  methods: {
    getProfPic(user_id) {
      if (this.comments !== null && this.user !== null && this.image !== null) {
        return this.users.filter((el) => el.user_id === user_id);
      }
    },
    getImgUrl1(pic) {
      if (pic) {
        // console.log(pic);
        return require("@/static/profile_picture/" + pic);
      }
    },
    usersFrom(comment) {
      if (this.comments !== null && this.user !== null && this.image !== null) {
        this.users.forEach((el) => {
          if (el.user_id === comment.comment_from) {
            // return el.prof_pic;
            this.comment_from = el.prof_pic;
          }
        });
      }
    },
  },
  computed: {
    image_ID() {
      return this.imageID;
    },
    image() {
      return this.$store.state.image;
    },
    user() {
      return this.$store.state.user;
    },
    users() {
      return this.$store.state.users;
    },
    comments() {
      return this.$store.state.comments;
    },

    commentDP() {
      return this.comment_profpic;
    },
  },
};
</script>

<style scoped>
* {
  font-size: 85%;
}
div {
  margin: 0;
  padding: 0;
}
span {
  margin-top: 0.5rem;
}
img {
  object-fit: cover;
  width: 1.5rem;
  height: 1.5rem;
  border-radius: 50%;
  border-style: none;
  margin-bottom: 0.5rem;
}
.comment__box {
  display: block;
  justify-content: center;
  align-items: center;
  background: #b3cde0;
  height: auto;
  width: 100%;
  margin-bottom: 0.5rem;
  margin-left: 0.5rem;
}

.row {
  display: flex;
  justify-content: center;
  align-items: center;
}
p {
  top: -10px;
  margin: 0;
  padding: 0;
  font-size: 120%;
}
.comments {
}

.post__comment .row {
  /* background: red; */
  width: 85%;
  margin: auto auto;
}
</style>
