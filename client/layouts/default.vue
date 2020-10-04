<template>
  <div>
    <AppMenu> </AppMenu>
    <div class="container">
      <nuxt />
    </div>
  </div>
</template>

<script>
import AppMenu from "../components/AppMenu";

export default {
  components: {
    AppMenu,
  },
};
</script>

<style>
body {
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
}

.container {
  padding: 0 20%;
}

h1 {
  text-align: center;
  font-size: 3em;
}

a {
  text-decoration: none;
  color: black;
}

a:hover {
  color: black;
}

.line {
  display: flex;
  justify-content: flex-end;
}

.btn {
  display: flex;
  align-items: center;
  background: rgb(111, 27, 167);
  padding: 15px 30px;
  color: white;
  border: none;
  border-radius: 3px;
}

input[type="text"],
input[type="password"],
input[type="text"]:-internal-autofill-selected,
input[type="passowrd"]:-internal-autofill-selected {
  width: 100%;
  padding: 10px;
  font-size: 1em;
  border: none;
  border-bottom: 2px solid black;
  display: inline-block;
  margin-bottom: 15px;
}
</style>
