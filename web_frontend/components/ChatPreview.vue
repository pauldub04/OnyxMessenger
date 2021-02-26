<template>
  <v-list-item class="ma-2">
    <v-list-item-avatar><v-img :src="userImage"></v-img></v-list-item-avatar>
    <v-list-item-content>
      <v-list-item-title>{{ username }}</v-list-item-title>
      <v-list-item-subtitle>{{ lastMessage }}</v-list-item-subtitle>
    </v-list-item-content>
    <v-list-item-action>
      <v-badge
        overlap
        :content="unreadMessages"
        :value="unreadMessages"
      ></v-badge>
      <v-list-item-action-text>{{ dateLastMessage }}</v-list-item-action-text>
    </v-list-item-action>
  </v-list-item>
</template>

<script>
export default {
  name: 'ChatPreview',
  props: {
    username: { type: String, default: undefined },
    userImage: {
      type: String,
      default:
        'https://cdn.iconscout.com/icon/free/png-512/account-269-866236.png',
    },
    lastMessage: { type: String, default: undefined },
    dateLastMessage: { type: String, default: undefined },
    unreadMessages: { type: Number, default: undefined },
  },
}
</script>

<style scoped></style>
