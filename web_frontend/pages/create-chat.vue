<template>
  <v-container fill-height>
    <v-container>
      <h1>Create Chat</h1>
      <v-stepper v-model="stepper" vertical>
        <v-stepper-step :complete="stepper > 1" step="1">
          Выберите тип чата:
        </v-stepper-step>
        <v-stepper-content step="1">
          <v-card flat color="#303030">
            <v-radio-group class="ml-2 mt-2 mb-0" v-model="newChatType">
              <v-radio
                v-for="(chat_type, idx) in chatType"
                :key="idx"
                :label="chat_type.name"
                :value="chat_type.val"
              ></v-radio>
            </v-radio-group>
          </v-card>
          <v-btn
            :disabled="newChatType === null"
            color="primary"
            @click="stepper = 2"
          >
            Continue
          </v-btn>
        </v-stepper-content>
        <v-stepper-step :complete="stepper > 2" step="2">
          Добавьте людей:
        </v-stepper-step>
        <v-stepper-content step="2">
          <v-container v-if="newChatType === 1">
            <v-autocomplete
              chips
              deletable-chips
              class="mt-4 mr-5"
              placeholder="Введите username"
              clearable
              label="Добавьте пользователя"
            ></v-autocomplete>
          </v-container>
          <v-container v-else>
            <v-autocomplete
              chips
              deletable-chips
              multiple
              class="mt-4 mr-5"
              placeholder="Введите username"
              clearable
              label="Добавьте пользователей"
            ></v-autocomplete>
          </v-container>
          <v-btn color="primary"> Create Chat </v-btn>
          <v-btn text @click="stepper = 1"> Cancel </v-btn>
        </v-stepper-content>
      </v-stepper>
    </v-container>
  </v-container>
</template>

<script>
// import {}
export default {
  name: 'CreateChat',
  data: () => ({
    stepper: 1,
    newChatType: null,
    inviteUserName: null,
    users: [],
    chatType: [
      {
        name: 'Личные сообщения',
        val: 1,
      },
      {
        name: 'Групповой чат',
        val: 2,
      },
    ],
  }),
}
</script>
