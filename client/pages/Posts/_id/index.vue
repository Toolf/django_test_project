<template>
  <div>
    <h1>{{ post.title }}</h1>
    <div class="content">
      <div v-for="(block, index) in post.content" :key="index">
        <p>{{ block }}</p>
      </div>
    </div>
    <div class="create_comment">
      <h3>New Comment:</h3>
      <textarea class="new_comment" v-model="new_comment"></textarea>
      <div class="line">
        <button class="btn" v-on:click="comment">Comment</button>
      </div>
    </div>
    <div class="comments">
      <div class="comment" v-for="comment in comments" :key="comment.id">
        <h3>{{ comment.user }}</h3>
        <p>{{ comment.content }}</p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      post: {},
      comments: [],
      new_comment: "",
    };
  },
  async created() {
    const config = {
      headers: {
        Accept: "application/json",
      },
    };

    try {
      const res = await axios.get(
        `http://localhost:8000/api/posts/${this.$route.params.id}/`,
        config
      );
      this.post = res.data;
      this.post.content = this.post.content.split("\n");
    } catch (err) {
      console.log(err);
    }
    this.comments = this.post.comments;
  },
  computed: {
    splitedContent() {
      let newArr = this.post.content.split("\n");
      return newArr;
    },
  },
  methods: {
    comment: async function () {
      const config = {
        headers: {
          Accept: "application/json",
          Authorization: `Token ${this.$store.state.token}`,
        },
      };

      try {
        console.log(config, this.new_comment);

        let res = await axios.post(
          `http://localhost:8000/api/comments/create/?type=post&post_id=${this.$route.params.id}`,
          {
            content: this.new_comment,
          },
          config
        );
        this.comments = [res.data, ...this.comments];
        this.new_comment = "";
        console.log(this.post.comments);
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>

<style>
.content {
  border-bottom: 5px dotted black;
  margin-bottom: 50px;
}

.comment {
  background-color: rgb(255, 255, 255);
  padding: 10px 30px;
  margin: 20px;
  border: 1px solid black;
  border-radius: 3px;
  color: rgb(0, 0, 0);
}

.new_comment {
  width: 100%;
  height: 100px;
  font-size: 1.5em;
  resize: none;
}
</style>
