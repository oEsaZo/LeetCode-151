class Solution {
    public List<List<Integer>> generate(int n) {
        List<List<Integer>> list=new ArrayList<>();
        List<Integer> p=new ArrayList<>();
        p.add(1);
        list.add(p);
        for(int i=0;i<n-1;i++){
            List<Integer> al=new ArrayList<>();
            List<Integer> temp=new ArrayList<>(list.get(i));
            al.add(1);
            for(int j=1;j<=i;j++){
                int sum=temp.get(j-1)+temp.get(j);
                al.add(sum);
            }
            al.add(1);
            list.add(al);
        }
        return list;
    }
}