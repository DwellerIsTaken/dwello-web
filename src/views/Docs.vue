<script setup>
import Footer from "../components/Footer.vue";
  import { ref } from "vue";
  
  let input = ref("");
  const fruits = ["apple", "banana", "orange"];
  function filteredList() {
    return fruits.filter((fruit) =>
      fruit.toLowerCase().includes(input.value.toLowerCase())
    );
  }
</script>

<template>
  <main>
    <div class="main mb-footer"> <!-- use mb-footer if you want to see footer-->
      <div class="w-col"></div>
        <div class="center">
          <h1 class="text-8xl my-28">Welcome to Dwello Docs.</h1>
          <div class="grid grid-cols-1 gap-4 mt-4">
            <div v-for="(value, key) in commands" :key="key" class="p-4 border rounded shadow-md">
              <h1 class="text-lg font-bold">{{ key }}</h1>
              <div v-for="(itemValue, itemKey) in value" :key="itemKey" class="mt-2">
                <h2 class="text-lg font-semibold">{{ itemKey }}</h2>
                <p v-html="formatText(itemValue.help)"></p>
              </div>
            </div>
          </div>
        </div>
      <div class="w-col"></div>
    </div>
    <Footer />
  </main>
</template>

<script>
export default {
  data() {
    return {
      commands: {}
    };
  },
  beforeMount() {
    this.fetchData();
  },
  methods: {
    fetchData() {
      fetch('http://localhost:8081/api/get', {
          method: 'GET',
          headers: {
            'Content-Type': 'application/json',
          }
        })
        .then(response => response.json())
        .then(data => {
          this.commands = data;
          console.log(data);
        })
        .catch(error => console.error('Error:', error));
    },
    formatText(text) {
      if (!text) return text;

      // Replace **bold** with <strong>bold</strong>
      text = text.replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>");

      // Replace __underscores__ with <em>underscores</em>
      text = text.replace(/__(.*?)__/g, "<em>$1</em>");

      // Replace [a link](url) with <a href="url">a link</a>
      //Doesnt remove the <> within (), so cant properly redirect?
      text = text.replace(/\[(.*?)\]\(([^)]+?)\)/g, '<a href="$2">$1</a>');
      console.log(text)

      return text;
    }
  },
};
</script>