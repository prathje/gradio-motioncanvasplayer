"""gr.HTML() component."""

from __future__ import annotations

from collections.abc import Callable, Sequence
from typing import TYPE_CHECKING, Any

from gradio_client.documentation import document

from gradio.components.base import Component
from gradio.events import Events
from gradio.i18n import I18nData

if TYPE_CHECKING:
    from gradio.components import Timer


class MotionCanvasPlayer(Component):
    """
    Creates a component to display arbitrary MotionCanvasPlayer output. As this component does not accept user input, it is rarely used as an input component.

    Demos: blocks_scroll
    Guides: key-features
    """

    EVENTS = [Events.change, Events.click]

    def __init__(
        self,
        value: str | Callable | None = None,
        *,
        label: str | I18nData | None = None,
        every: Timer | float | None = None,
        inputs: Component | Sequence[Component] | set[Component] | None = None,
        show_label: bool = False,
        visible: bool = True,
        elem_id: str | None = None,
        elem_classes: list[str] | str | None = None,
        render: bool = True,
        key: int | str | tuple[int | str, ...] | None = None,
        preserved_by_key: list[str] | str | None = "value",
        min_height: int | None = None,
        max_height: int | None = None,
        container: bool = False,
        padding: bool = True,
        auto: bool | None = False,
        quality: number | None = None,
        width: int | None = None,
        height: int | None = None,
        variables: str | None = None,
    ):
        """
        Parameters:
            value: The MotionCanvasPlayer content to display. Only static MotionCanvasPlayer is rendered (e.g. no JavaScript. To render JavaScript, use the `js` or `head` parameters in the `Blocks` constructor). If a function is provided, the function will be called each time the app loads to set the initial value of this component.
            label: The label for this component. Is used as the header if there are a table of examples for this component. If None and used in a `gr.Interface`, the label will be the name of the parameter this component is assigned to.
            every: Continously calls `value` to recalculate it if `value` is a function (has no effect otherwise). Can provide a Timer whose tick resets `value`, or a float that provides the regular interval for the reset Timer.
            inputs: Components that are used as inputs to calculate `value` if `value` is a function (has no effect otherwise). `value` is recalculated any time the inputs change.
            show_label: If True, the label will be displayed. If False, the label will be hidden.
            visible: If False, component will be hidden.
            elem_id: An optional string that is assigned as the id of this component in the MotionCanvasPlayer DOM. Can be used for targeting CSS styles.
            elem_classes: An optional list of strings that are assigned as the classes of this component in the MotionCanvasPlayer DOM. Can be used for targeting CSS styles.
            render: If False, component will not render be rendered in the Blocks context. Should be used if the intention is to assign event listeners now but render the component later.
            key: in a gr.render, Components with the same key across re-renders are treated as the same component, not a new component. Properties set in 'preserved_by_key' are not reset across a re-render.
            preserved_by_key: A list of parameters from this component's constructor. Inside a gr.render() function, if a component is re-rendered with the same key, these (and only these) parameters will be preserved in the UI (if they have been changed by the user or an event listener) instead of re-rendered based on the values provided during constructor.
            min_height: The minimum height of the component, specified in pixels if a number is passed, or in CSS units if a string is passed. If MotionCanvasPlayer content exceeds the height, the component will expand to fit the content.
            max_height: The maximum height of the component, specified in pixels if a number is passed, or in CSS units if a string is passed. If content exceeds the height, the component will scroll.
            container: If True, the MotionCanvasPlayer component will be displayed in a container. Default is False.
            padding: If True, the MotionCanvasPlayer component will have a certain padding (set by the `--block-padding` CSS variable) in all directions. Default is True.
            auto: If True, the MotionCanvasPlayer component will automatically play the animation. Default is False.
            quality: The quality of the MotionCanvasPlayer component. Default is None which uses the project's default settings.
            width: The width of the MotionCanvasPlayer component. Default is None which uses the project's default settings.
            height: The height of the MotionCanvasPlayer component. Default is None which uses the project's default settings.
            variables: The variables of the MotionCanvasPlayer component as a JSON string. Default is None.
        """
        self.min_height = min_height
        self.max_height = max_height
        self.padding = padding

        self.auto = auto
        self.quality = quality
        self.width = width
        self.height = height
        self.variables = variables


        super().__init__(
            label=label,
            every=every,
            inputs=inputs,
            show_label=show_label,
            visible=visible,
            elem_id=elem_id,
            elem_classes=elem_classes,
            render=render,
            key=key,
            preserved_by_key=preserved_by_key,
            value=value,
            container=container,
        )

    def example_payload(self) -> Any:
        return "<p>Hello</p>"

    def example_value(self) -> Any:
        return "<p>Hello</p>"

    def preprocess(self, payload: str | None) -> str | None:
        """
        Parameters:
            payload: string corresponding to the MotionCanvasPlayer
        Returns:
            (Rarely used) passes the MotionCanvasPlayer as a `str`.
        """
        return payload

    def postprocess(self, value: str | None) -> str | None:
        """
        Parameters:
            value: Expects a `str` consisting of valid MotionCanvasPlayer.
        Returns:
            Returns the MotionCanvasPlayer string.
        """
        return value

    def api_info(self) -> dict[str, Any]:
        return {"type": "string"}
