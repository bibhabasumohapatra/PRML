import torch


class Polynomial:
    def __init__(self, degree):
        # Initialize coefficients as learnable parameters
        self.coef = torch.randn(degree + 1, requires_grad=True)

    def __call__(self, x):
        # Evaluate the polynomial at the given value(s) of x
        self.powers = torch.arange(len(self.coef)).float()
        return torch.sum(self.coef * x.unsqueeze(-1).pow(powers), dim=-1)

    def parameters(self):
        # Return the list of parameters (coefficients)
        return self.coef
    
    def get_variables(self,x):

        return x.unsqueeze(-1).pow(self.powers)
    
    def __repr__(self):
        """
        Return a string representation of the polynomial.
        """
        terms = []
        for i, c in enumerate(self.coef):
            if i == 0:
                terms.append(f"{c.item()}")
            else:
                terms.append(f"{c.item()} * x^{i}")
        return " + ".join(terms)

