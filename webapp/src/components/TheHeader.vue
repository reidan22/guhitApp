<template>
  <header>
    <ul>
      <li class="logo_nav">
        <router-link to="/feed">Guhit</router-link>
      </li>
      <!-- <li><a href="#">Gallery</a></li> -->
      <li>
        {{ $store.state.user.user_id }}
      </li>
      <li @click="openUpdateForm" class="feed__dp">
        <feed-dp></feed-dp>
      </li>
      <li>
        <router-link to="/user">Gallery</router-link>
      </li>
      <li @click="logout">
        <router-link to="/">Logout</router-link>
      </li>
    </ul>
    <div v-if="isUpdateFormVisible" class="update round__border">
      <div class="container">
        <div class="row dpin">
          <input
            type="file"
            @change="previewFiles"
            id="file"
            label
            style="none"
            class="id"
          />
        </div>
        <div class="row">
          <label for="title">Title</label>
          <input type="text" name="title" id="title" v-model="title" />
        </div>
        <div class="row">
          <label for="caption">Caption</label>
          <input type="text" name="caption" id="caption" v-model="caption" />
        </div>
        <div class="row">
          <button type="submit" @click="addPost">Post</button>
        </div>
      </div>
    </div>
  </header>
</template>

<script>
import FeedDP from "./FeedDP.vue";
export default {
  components: {
    "feed-dp": FeedDP,
  },
  data: function() {
    return {
      isUpdateFormVisible: false,
      title: null,
      caption: null,
      fileSelected: null,
    };
  },

  methods: {
    async updateUser(load) {
      await fetch("http://127.0.0.1:5000/api/images", {
        method: "POST",
        body: JSON.stringify(load),
        headers: {
          "Content-type": "application/json; charset=UTF-8",
        },
      });
    },
    addPost() {
      if (this.fileSelected === "" || this.fileSelected === null) {
        this.fileSelected = "default_pic.png";
      }
      if (!this.fileSelected) {
        this.fileSelected = "default_pic.png";
      }
      var x = {
        id: this.$store.state.images.length + 1,
        user_id: this.$store.state.user.user_id,
        title: this.title,
        caption: this.caption,
        image_file: this.fileSelected,
        likes: [""],
      };
      this.updateUser(x);
      this.isUpdateFormVisible = false;
      console.log(x);
    },
    previewFiles(e) {
      this.fileSelected = e.target.files[0].name;
      // alert(this.fileSelected);
    },
    openUpdateForm() {
      this.isUpdateFormVisible = !this.isUpdateFormVisible;
      // alert(this.isUpdateFormVisible);
    },
    logout() {
      this.$store.commit("changeIsLogin");
    },
  },
};
</script>

<style scoped>
.row {
  margin-top: 0.5rem;
}
.container {
  display: block;
  justify-content: center;
  align-content: center;
}
.feed__dp {
  transition: 0.25s;
}
.feed__dp:hover {
  transform: scale(0.95);
  opacity: 0.85;
}
.update {
  display: flex;
  position: absolute;
  justify-content: center;
  align-content: center;
  background-color: #011f4b;
  color: #b3cde0;
  width: 11rem;
  left: 34rem;
  z-index: 10;
}
ul {
  list-style: none;
  display: flex;
  justify-content: flex-end;
  align-items: center;
  margin: 0;
  padding: 0px;
}

li {
  justify-content: flex-end;
  align-items: flex-end;
  padding: 1rem;
  color: #b3cde0;
  font-size: 65%;
}

a {
  text-decoration: none;
  color: #b3cde0;
  transition: 0.25s;
}
a:hover {
  color: #6497b1;
}

.logo_nav {
  font-family: Brushes;
  margin-right: auto;
  font-size: 80%;
}
ul {
  background-image: url("./../assets/img/bg.jpg");

  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  width: 100vw;
}

.front-bg {
  background-color: #005b96;
  height: 100vh;
}
button,
label,
input {
  height: auto;
  width: 50%;
  margin: auto auto;
  padding-top: 0.25rem;
}
label,
button {
  width: 4rem;
}
input,
button {
  font-size: 0.5rem;
  height: 1rem;
}
.id {
  transform: scale(0.5);
  height: 2rem;
}
.dpin {
  font-size: 2rem;
}
label {
  font-size: 0.5rem;
}
button {
  margin-bottom: 1rem;
}
</style>
