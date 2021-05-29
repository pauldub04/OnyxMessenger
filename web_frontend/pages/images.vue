<template>
  <v-app>
    <h3>Upload image</h3>
    <v-file-input v-model="file"></v-file-input>
    <v-btn @click="upload">Upload</v-btn>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    chatName: '',
    file: null,
  }),
  methods: {
    upload() {
      console.log(this.file)
      const formData = new FormData()
      formData.append('image', this.file)
      formData.append('title', 'dfg')
      formData.append('type', 1)
      formData.append('users', [])

      this.$axios
        .post('http://localhost:8000/api/chats/', formData)
        .then((response) => {
          console.log(response.data)
          this.$router.push('/main')
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}
</script>
