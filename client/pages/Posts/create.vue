<template>
  <div>
    <h1>Create Post</h1>
    <input type="text" name="title" placeholder="Title" v-model="title" />
    <textarea v-model="content" name="content" class="content__area"></textarea>
    <div class="line">
      <button class="btn" v-on:click="newPost">Submit</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      title: "",
      content: "",
    };
  },
  methods: {
    async newPost() {
      let url = "http://localhost:8000/api/posts/create/";
      const config = {
        headers: {
          Accept: "application/json",
          Authorization: `Token ${this.$store.state.token}`,
        },
      };

      try {
        const res = await axios.post(
          url,
          {
            title: this.title,
            content: this.content,
          },
          config
        );
        alert("Post was created");
        console.log(res.data);
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>

<style>
.content__area {
  width: 100%;
  height: 500px;
  font-size: 2em;
}
</style>