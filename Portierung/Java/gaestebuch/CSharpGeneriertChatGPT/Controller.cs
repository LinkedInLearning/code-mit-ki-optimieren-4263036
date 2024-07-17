public class Controller {
    private Model model;
    private View view;

    public Controller(Model model, View view) {
        this.model = model;
        this.view = view;
    }

    public void UpdateView() {
        view.PrintDetails(model.GetName(), model.GetValue());
    }

    public void SetModelName(string name) {
        model.SetName(name);
    }

    public void SetModelValue(int value) {
        model.SetValue(value);
    }
}
