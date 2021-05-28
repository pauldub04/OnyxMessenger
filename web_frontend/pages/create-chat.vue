<template>
  <v-container fill-height>
    <v-container>
      <h1>Создание чата</h1>
      <v-stepper v-model="stepper" class="mt-5" vertical>
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
            Далее
          </v-btn>
          <v-btn text to="/main"> Отмена </v-btn>
        </v-stepper-content>
        <v-stepper-step :complete="stepper > 2" step="2">
          Добавьте людей:
        </v-stepper-step>
        <v-stepper-content step="2">
          <v-container v-if="newChatType === 1">
            <v-autocomplete
              :items="users"
              v-model="inviteUserName"
              class="mt-4 mr-5"
              placeholder="Введите username"
              clearable
              label="Выберите пользователя"
            ></v-autocomplete>
          </v-container>
          <v-container v-else>
            <v-autocomplete
              :items="users"
              v-model="inviteUserName"
              chips
              deletable-chips
              multiple
              class="mt-4 mr-5"
              placeholder="Введите username"
              clearable
              label="Добавьте пользователей"
            ></v-autocomplete>
          </v-container>
          <v-btn
            color="primary"
            @click="createChat"
            v-if="newChatType == 1"
            :disabled="inviteUserName === null"
          >
            Создать чат
          </v-btn>
          <v-btn color="primary" @click="stepper = 3" v-else> Далее </v-btn>
          <v-btn text @click="stepper = 1"> Назад </v-btn>
        </v-stepper-content>

        <div v-if="newChatType == 2">
          <v-stepper-step :complete="stepper > 3" step="3">
            Название чата:
          </v-stepper-step>
          <v-stepper-content step="3">
            <v-form v-model="valid">
              <v-text-field
                label="Название чата"
                v-model="chatName"
                :rules="[(v) => !!v || 'Введите название']"
                required
                clearable
              ></v-text-field>
              <v-btn color="primary" @click="createChat" :disabled="!valid">
                Создать чат
              </v-btn>
              <v-btn text @click="stepper = 1"> Назад </v-btn>
            </v-form>
          </v-stepper-content>
        </div>
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
    chatName: null,
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

    valid: false,
  }),
  created() {
    this.getUsers()
  },
  methods: {
    createChat() {
      if (this.newChatType === 1) {
        this.chatName = this.inviteUserName

        const tmp = this.inviteUserName
        this.inviteUserName = []
        this.inviteUserName.push(tmp)
      }
      console.log(this.newChatType)
      console.log(this.inviteUserName)
      console.log(this.chatName)

      this.$axios
        .post('http://localhost:8000/api/chats/', {
          type: this.newChatType,
          users: this.inviteUserName,
          title: this.chatName,
        })
        .then((response) => {
          console.log(response.data)
          this.$router.push('/main')
        })
        .catch((error) => {
          console.log(error)
        })
    },
    getUsers() {
      this.$axios
        .get(`http://127.0.0.1:8000/api/users/all/`)
        .then((response) => {
          this.users = response.data.users
        })
        .catch((error) => {
          console.log(error)
        })
    },
  },
}
</script>
