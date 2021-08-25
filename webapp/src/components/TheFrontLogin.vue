<template>
  <form
    id="form1"
    method="get"
    type="submit"
    value="Submit"
    @submit="checkForm"
  >
    <div class="drop__shadow round__border bg">
      <div class="container">
        <div class="row head">{{ tabSelected }}</div>
        <div class="row input__login" v-if="loginTabSelected">
          <label for="username">Username</label>
          <input
            class="round__border"
            type="text"
            id="username"
            name="username"
            required
            v-model="username"
          />
          <label for="pword">Password</label>
          <input
            class="round__border"
            type="password"
            id="pword"
            name="pword"
            required
            v-model="password"
          />
          <button
            class="round__border"
            type="submit"
            value="Submit"
            form="form1"
          >
            Sign-in
          </button>
        </div>
        <div class="row input__register" v-if="regTabSelected">
          <label for="username_reg">Username</label>
          <input
            class="round__border"
            type="text"
            id="username_reg"
            name="username_reg"
            required
            v-model="regUsername"
          />
          <label for="email">Email</label>
          <input
            class="round__border"
            type="email"
            id="email"
            name="email"
            v-model="regEmail"
            required
          />
          <label for="pword_reg">Password</label>
          <input
            class="round__border"
            type="password"
            id="pword_reg"
            name="pword_reg"
            required
            v-model="regPassword"
          />
          <label for="conf_pword_reg">Confirm Password</label>
          <input
            class="round__border"
            type="password"
            id="conf_pword_reg"
            name="conf_pword_reg"
            required
            v-model="regConfPassword"
          />
          <label for="prof_pic">DP</label>
          <input
            class="round__border"
            type="file"
            id="file"
            name="file"
            @change="previewFiles"
            required
          />
          <button
            class="round__border"
            type="submit"
            value="Submit"
            form="form1"
          >
            Register
          </button>
        </div>
      </div>

      <div class="bottom__tab">
        <div
          @click="selectLogin"
          :class="[
            `bottom__tab__left`,
            { active: loginTabSelected, inactive: regTabSelected },
          ]"
        >
          Login
        </div>
        <div
          @click="selectReg"
          :class="[
            `bottom__tab__right`,
            { inactive: loginTabSelected, active: regTabSelected },
          ]"
        >
          Register
        </div>
      </div>
    </div>
  </form>
</template>

<script>
export default {
  data: function() {
    return {
      tabSelected: "Login",
      loginTabSelected: true,
      regTabSelected: false,
      regUsername: null,
      regEmail: null,
      regPassword: null,
      regConfPassword: null,
      prof_pic: "default_pic.png",
      fileSelected: null,
      username: null,
      password: null,
    };
  },
  methods: {
    previewFiles(e) {
      this.fileSelected = e.target.files[0].name;
      // alert(this.fileSelected);
    },
    async postUser(load) {
      await fetch("http://127.0.0.1:5000/api/users", {
        method: "POST",
        body: JSON.stringify(load),
        headers: { "Content-type": "application/json; charset=UTF-8" },
      });
      // console.log(load);
    },
    resetVals() {
      this.tabSelected = "Login";
      this.loginTabSelected = true;
      this.regTabSelected = false;
      this.regUsername = null;
      this.regEmail = null;
      this.regPassword = null;
      this.regConfPassword = null;
    },
    selectLogin() {
      this.loginTabSelected = true;
      this.regTabSelected = false;
      this.tabSelected = "Login";
    },
    selectReg() {
      this.regTabSelected = true;
      this.loginTabSelected = false;
      this.tabSelected = "Register";
    },
    checkLogin() {
      this.$store.commit("getLoginInfo", {
        username: this.username,
        password: this.password,
      });
      const users = this.users;
      let current_user = null;
      let bool_user = false;
      users.forEach((user) => {
        if (user["user_id"] === this.$store.state.username) {
          current_user = user;
          this.$store.commit("getUser", user);
        }
      });
      if (current_user) {
        if (current_user["password"] === this.$store.state.password) {
          return true;
        } else {
          alert("Incorrect password! Try again.");
          return false;
        }
      } else if (!this.regTabSelected) {
        alert("Username does not exist! Try again.");
        return false;
      }
    },
    checkForm(e) {
      if (
        this.regUsername &&
        this.regEmail &&
        this.regPassword &&
        this.regConfPassword &&
        this.regTabSelected
      ) {
        if (this.regPassword === this.regConfPassword) {
          let x = {
            id: this.users.length + 1,
            user_id: this.regUsername,
            fname: "Juan",
            lname: "dela Cruz",
            email: this.regEmail,
            password: this.regPassword,
            prof_pic: this.fileSelected,
          };
          console.log("REGISTREING", x);
          this.postUser(x);

          this.$store.commit("getUsers");
          alert("Registration complete!");

          // this
        } else {
          alert("Password mismatched! Try again.");
          this.resetVals();
        }
      } else if (this.username && this.password && this.loginTabSelected) {
      }
      if (this.checkLogin()) {
        this.$store.commit("changeIsLogin");
      }
      this.resetVals();

      e.preventDefault();
    },
  },
  computed: {
    loginSelected() {
      return this.loginTabSelected;
    },
    regSelected() {
      return this.regTabSelected;
    },
    users() {
      return this.$store.state.users;
    },
  },
};
</script>

<style scoped>
* {
  outline: none;
  border: none;
}
.bg {
  width: 12rem;
  height: 18rem;
  background-color: #b3cde0;
  /* border-bottom-left-radius: 0;
  border-bottom-right-radius: 0; */
  overflow: hidden;
}

.head {
  font-family: Brushes;
  font-size: 120%;
  display: flex;
  justify-content: center;
  align-items: top;
  margin: 1rem 5px;
}

.row {
  display: flex;
  justify-content: center;
}

button {
  position: relative;
  top: 1rem;
  background-color: #03396c;
  color: #b3cde0;
  transition: 0.2s;
  padding: 5px 10px;

  width: 4rem;
  height: 1rem;
  font-size: 50%;
}

button:hover {
  transform: scale(0.95);
}

input {
  padding: 5px 10px;
  width: 80%;
  height: 70%;
}
label {
  font-size: 65%;
  display: flex;
  justify-content: flex-start;
}

.input__register input {
  height: 10%;
  font-size: 75%;
}

.container {
  height: 87%;
}
.bottom__tab {
  margin: 0;
  /* position: relative; */
  top: 6.3rem;
  display: inline-flex;
  width: 101%;
  justify-content: center;
  align-items: center;
  font-size: 75%;
}
.bottom__tab__left {
  width: 100%;
  height: 10%;
}

.bottom__tab__right {
  width: 100%;
  height: 10%;
}

.active {
  background: #b3cde0;
  color: #03396c;
  opacity: 100%;
}

.inactive {
  background: #03396c;
  color: #b3cde0;
  opacity: 85%;
}
</style>
