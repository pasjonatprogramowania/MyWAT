<template>
  <div class="q-pa-lg">
    <h5>Opcje</h5>
    <q-list bordered class="prounded-borders">
      <q-expansion-item
        expand-separator
        icon="event"
        label="Typ wydarzenia"
      >
        <q-option-group
          v-model="group"
          :options="options"
          color="primary"
          class="q-pa-sm"
          type="checkbox"
        />
      </q-expansion-item>
    </q-list>
    <q-expansion-item
      expand-separator
      icon="place"

      label="Dodawanie punktów"
    >
      <div class="q-pa-sm">


      <q-btn
        color="primary"
        text-color="white"
        label="Dodaj"
        @click="emit('addPoint')"
      />
      <q-btn
        color="primary"
        text-color="white"
        label="Usuń"
        @click="emit('removePoint')"
      />
      <q-btn
        color="primary"
        text-color="white"
        label="Popraw"
        @click="emit('correctPoint')"
      />
      </div>
    </q-expansion-item>
    <q-expansion-item class="q-pa-sm" expand-separator icon="local_shipping" label="Przejazdy">
      <TimeInput></TimeInput>
      <q-btn color="primary" text-color="white" label="Pokaż" />
    </q-expansion-item>
  </div>
</template>

<script setup>
import { ref, defineEmits } from "vue";
import TimeInput from "components/TimeInput.vue";

const emit = defineEmits(["addPoint", "removePoint", "correctPoint"]);
const group = ref(["kz"]);

const options = ref([
  {
    label: "Koła zainteresowań ",
    value: "kz",
  },
  {
    label: "Imprezy eventy watowe",
    value: "iw",
  },
  {
    label: "Ogłoszenia",
    value: "og",
  },
]);
</script>
