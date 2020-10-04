<template>
  <div>
    <h1>Login</h1>
    <div class="login">
      <label for="username">Username</label>
      <input
        v-model="username"
        type="text"
        placeholder="Enter Username"
        name="username"
        required
      />

      <label for="password">Password</label>
      <input
        v-model="password"
        type="password"
        placeholder="Enter password"
        name="password"
        required
      />

      <button class="login__btn" v-on:click="login">Login</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  computed: {
    token() {
      return this.$store.state.token;
    },
  },
  methods: {
    login: async function () {
      try {
        const res = await axios.post(
          "http://localhost:8000/auth/token/login/",
          {
            username: this.username,
            password: this.password,
          }
        );
        this.$store.commit("login", res.data.auth_token);
        this.$router.push("/posts/");
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>

<style>
.login {
  padding: 30px 20%;
}

.login__btn {
  width: 100%;
  padding: 15px;
  font-size: 2em;
  border: 5px solid rgb(100, 58, 179);
  border-radius: 3px;
  font-weight: bold;
  color: rgb(100, 58, 179);
  background: white;
}

.login__btn:active {
  background-color: rgb(100, 58, 179);
  color: white;
}
</style>
