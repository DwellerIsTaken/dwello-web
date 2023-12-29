<script setup>
  import NavBar from "../components/NavBar.vue";
  import Footer from "../components/Footer.vue";
  import { ref, onMounted, onBeforeUnmount } from "vue";

  const dimmingText = ref(null);

  /*onMounted(() => {
    dimmingText.value.style.opacity = "1";

    const updateOpacity = () => {
      const scrollPercentage =
        scrollY.value / (document.body.scrollHeight - window.innerHeight);
      let opacity = 1 - scrollPercentage;

      opacity = Math.min(1, Math.max(0, opacity));

      dimmingText.value.style.opacity = opacity.toFixed(2);
    };

    window.addEventListener("scroll", updateOpacity);

    onBeforeUnmount(() => {
      window.removeEventListener("scroll", updateOpacity);
    });
  });*/
</script>

<template>
    <div class="main">
      <div class="col"></div>
      <div class="center">
        <NavBar />
        <div class="py-80 flex flex-col items-center justify-center text-9xl opacity-100 transition-opacity duration-500 animate-fadeup" ref="dimmingText">
          <h1 class="font-kanit">Looking for a cool Discord Bot? <a class="underline selection:decoration-white" href="#">Invite me.</a></h1>
          <!--somehow add a newline when screen gets too wide in order to keep second sentence on a new line.-->
          <!--when selecting the black background can overlap some of the selected text above; at least for big headers.-->
        </div>
        <div class="w-full flex relative mb-10">
          <div class="left">
            <h1 class="text-8xl mb-6">Invite me, please.</h1>
            <p>
              Exciting news, Discord enthusiasts! Meet Dwello – your server's new
              dynamic companion, ready to revolutionize your Discord adventures.
              Dwello isn't just your typical bot; think of it as a
              hyper-energetic, tech-savvy sidekick with lightning-fast responses,
              rivaling a cheetah on a caffeine rush! We're so thrilled about this
              launch that our coffee mugs are getting more attention than our
              inboxes. But that's not all – Dwello boasts features so fantastic
              they make unicorns jealous, from meme-tastic commands to server
              management magic. Now, we're not just here to brag; we need your
              help to spread the joy Picture Dwello as the friend always up for a
              good time, and all we ask is for you to invite this digital dynamo
              to your server. Your support means the world, and Dwello promises to
              transform your server into the coolest spot in the Discord universe.
              So, what are you waiting for? Let's turn those servers into
              Dwello-icious hotspots together!
            </p>
            <div class="flex justify-between gap-5">
              <a href="#" class="text-4xl p-4 mt-8 rounded border-4 border-solid border-black flex relative transition-transform duration-700 hover:scale-105">Invite to the server</a>
              <a href="#" class="text-4xl p-4 mt-8 rounded border-4 border-solid border-black flex relative transition-transform duration-700 hover:scale-105">See features</a>
            </div>
          </div>
          <div class="right-center">
            <img
              class="mt-7"
              src="/src/assets/discord.svg"
              alt="Discord Logo"
              width="500"
              height="500"
            />
          </div>
        </div>
      </div>
      <div class="col"></div>
    </div>
    <Footer />
</template>
