<template>
  <div class="user__page">
    <div class="row ">
      <div class="col bg drop__shadow big">
        <div class="row time">{{ timestamp }}</div>
        <div class="row ">
          <user-page-dp></user-page-dp>
        </div>
        <!-- <div class="row name">{{ fname }} {{ lname }}</div> -->
      </div>
      <div class="col user__img">
        <user-page-images></user-page-images>
      </div>
    </div>
  </div>
</template>

<script>
import UserPageDP from "../UserPageDP.vue";
import UserPageImages from "../UserPageImages.vue";
export default {
  data: function() {
    return { timestamp: "" };
  },
  components: {
    "user-page-dp": UserPageDP,
    "user-page-images": UserPageImages,
  },
  created() {
    setInterval(this.getNow, 1000);
  },
  methods: {
    getNow() {
      const today = new Date();
      const date =
        today.getFullYear() +
        "/" +
        (today.getMonth() + 1).toString().padStart(2, "0") +
        "/" +
        today
          .getDate()
          .toString()
          .padStart(2, "0");
      const time =
        today
          .getHours()
          .toString()
          .padStart(2, "0") +
        ":" +
        today
          .getMinutes()
          .toString()
          .padStart(2, "0") +
        ":" +
        today
          .getSeconds()
          .toString()
          .padStart(2, "0");
      const dateTime = date + " " + time;
      this.timestamp = dateTime;
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
.row {
  display: flex;
  justify-content: center;
  align-items: center;
}

.bg {
  background: #011f4bb4;
  height: 70vh;
  border-radius: 5%;
  margin-left: 1rem;
}
.name,
.time {
  color: #b3cde0;
  font-size: 150%;
}
.time {
  font-size: 200%;
  margin-top: 1rem;
}
.big {
  margin: 2rem 20px;
}
</style>
