<template>
  <div class="fluid-container">
    <div class="row">
      <span class="img" v-for="image in filterImages">
        <router-link :to="`/image/` + image.id">
          <img
            @click="passImage(image)"
            :src="getImgUrl(image.image_file)"
            alt="Image file."
          />
        </router-link>
      </span>
    </div>
    <!-- <div class="row">
      <div class="row">
        <label for="addcomment">Title</label>
        <input
          type="textarea"
          id="addcomment"
          name="addcomment"
          rows="20"
          cols="20"
          v-model="title"
        />
      </div>
      <div class="row">
        <label for="addcomment">Caption</label>
        <input
          type="textarea"
          id="addcomment"
          name="addcomment"
          rows="20"
          cols="20"
          v-model="caption"
        />
      </div>
      <input type="file" @change="previewFiles" id="file" label style="none" />
      <button type="submit" @click="submitFile">Add</button>
    </div> -->
  </div>
</template>

<script>
export default {
  data: function() {
    return {
      fileSelected: null,
      title: null,
      caption: null,
    };
  },
  methods: {
    async postImage(load) {
      await fetch("http://127.0.0.1:5000/api/images", {
        method: "POST",
        body: JSON.stringify(load),
        headers: { "Content-type": "application/json; charset=UTF-8" },
      });
    },
    addImage(e) {
      let x = {
        id: this.images.length + 1,
        user_id: this.user.user_id,
        title: this.title,
        caption: this.caption,
        image_file: this.fileSelected,
        likes: [""],
      };
      console.log(x);
      this.postImage(x);

      // alert("Comment added!");
      this.title = null;
      this.caption = null;
      this.fileSelected = null;
    },
    submitFile() {
      if (this.fileSelected) {
        alert("Uploading " + this.fileSelected);
        this.addImage();
      }
    },
    previewFiles(e) {
      this.fileSelected = e.target.files[0].name;
      // alert(this.fileSelected);
    },
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
    images() {
      return this.$store.state.images;
    },
    user() {
      return this.$store.state.user;
    },
    filterImages() {
      if (this.images !== null && this.user !== null) {
        return this.images
          .filter((el) => el.user_id === this.user.user_id)
          .reverse();
      }
    },
  },
};
</script>

<style scoped>
.fluid-container {
  width: 20rem;
  height: 20rem;
  overflow-y: auto;
  overflow-x: none;
  overflow: hidden;
  display: block;
  padding: 1rem;
}

img {
  border: 0.25rem solid white;
  height: 5rem;
  margin: 0.1rem;
  transition: 0.25s;
}

img:hover {
  transform: scale(0.95);
}

.img {
  margin: 0;
  padding: 0;
}
input {
  transform: scale(0.5);
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
  width: 10%;
  height: 70%;
  font-size: 30%;
}
label {
  display: flex;
  justify-content: center;
  font-size: 20px;
}

.row {
  display: block;
  overflow-x: hidden;
}
</style>
