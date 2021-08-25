<template>
  <div class="col-4 comments">
    <span v-for="comment in filterComments">
      <div class="fluid-container">
        <div class="row">
          <div class="col-2">
            {{ usersFrom(comment) }}
            <img :src="getImgUrl(comment_from)" alt="" />
          </div>
          <div class="col-10 comment__box round__border">
            <p>{{ comment.comment_from }}</p>
            {{ comment.comment }}
          </div>
          <div class="row add__comment"></div>
        </div>
      </div>
    </span>
    <div class="row">
      <div class="row">
        <label for="addcomment">Add Comment</label>
      </div>
      <div class="row">
        <input
          type="textarea"
          id="addcomment"
          name="addcomment"
          rows="20"
          cols="20"
          v-model="toAddComment"
        />
      </div>
      <button @click="addComment" class="round__border" type="submit">
        Add
      </button>
    </div>
  </div>
</template>

<script>
export default {
  props: ["photo"],
  data: function() {
    return { comment_from: null, toAddComment: "" };
  },
  methods: {
    async postComment(load) {
      await fetch("http://127.0.0.1:5000/api/comments", {
        method: "POST",
        body: JSON.stringify(load),
        headers: { "Content-type": "application/json; charset=UTF-8" },
      });
    },
    addComment(e) {
      let x = {
        id: this.comments.length + 1,
        img_id: this.photo.id,
        comment: this.toAddComment,
        comment_from: this.$store.state.user.user_id,
        date_posted: "Date",
      };
      // console.log(x);
      this.postComment(x);

      // alert("Comment added!");
      this.toAddComment = "";
    },
    getImgUrl(pic) {
      if (pic) {
        return require("@/static/profile_picture/" + pic);
      }
    },
    usersFrom(comment) {
      if (this.comments !== null && this.user !== null && this.photo !== null) {
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
    filterComments() {
      if (this.comments !== null && this.user !== null && this.photo !== null) {
        return this.comments.filter((el) => el.img_id === this.photo.id);
      }
    },
  },
};
</script>

<style scoped>
* {
  font-size: 85%;
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
  display: flex;
  justify-content: flex-start;
  align-items: center;
  background: #b3cde0;
  height: auto;
  width: 75%;
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
}
button {
  position: relative;
  background-color: #03396c;
  color: #b3cde0;
  transition: 0.2s;
}

button:hover {
  transform: scale(0.95);
}

input {
  width: 80%;
}

button {
  width: 40%;
  height: 70%;
}
label {
  display: flex;
  justify-content: center;
}
</style>
