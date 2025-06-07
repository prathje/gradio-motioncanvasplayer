<script lang="ts">
	import { createEventDispatcher } from "svelte";
	import '@motion-canvas/player';
	export let elem_classes: string[] = [];
	export let value: string;
	export let width: number | undefined;
	export let height: number | undefined;
	export let auto: boolean | undefined;
	export let quality: number | undefined;
	export let variables: string | undefined;

	export let visible = true;

	const dispatch = createEventDispatcher<{
		change: undefined;
		click: undefined;
	}>();

	$: value, dispatch("change");
</script>

<!-- svelte-ignore a11y-click-events-have-key-events a11y-no-static-element-interactions -->
<div
	class="prose {elem_classes.join(' ')}"
	class:hide={!visible}
	on:click={() => dispatch("click")}
>
	Debug: { value }
	<!-- See https://github.com/motion-canvas/motion-canvas/blob/main/packages/player/types/main.d.ts for supported props -->
	{#if value}
		<motion-canvas-player
			src={value}
			width={width}
			height={height}
			auto={auto}
			quality={quality}
			variables={variables}
		></motion-canvas-player>
	{/if}
</div>

<style>
	.hide {
		display: none;
	}
</style>
